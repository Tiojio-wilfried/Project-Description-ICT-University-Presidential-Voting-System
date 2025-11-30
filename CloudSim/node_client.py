"""
Node Client - Représente un nœud de stockage qui se connecte au cloud
Lance ce fichier dans un terminal séparé pour chaque nœud
"""
import socket
import json
import sys
import time
import argparse

class StorageNode:
    def __init__(self, node_id: str, cpu: int, memory: int, storage: int, bandwidth: int, 
                 cloud_host='localhost', cloud_port=5000):
        self.node_id = node_id
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.bandwidth = bandwidth
        self.cloud_host = cloud_host
        self.cloud_port = cloud_port
        
        # Attribué par le cloud
        self.ip_address = None
        self.mac_address = None
        self.connected = False
        
    def connect_to_cloud(self):
        """Se connecte au cloud et obtient IP + MAC"""
        try:
            print(f"[{self.node_id}] Connexion au cloud {self.cloud_host}:{self.cloud_port}...")
            
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.cloud_host, self.cloud_port))
            
            # Envoyer les informations du nœud
            register_request = {
                'type': 'REGISTER',
                'node_id': self.node_id,
                'node_info': {
                    'cpu': self.cpu,
                    'memory': self.memory,
                    'storage': self.storage,
                    'bandwidth': self.bandwidth
                }
            }
            
            self.socket.send(json.dumps(register_request).encode('utf-8'))
            
            # Recevoir la réponse du cloud
            response = self.socket.recv(4096).decode('utf-8')
            data = json.loads(response)
            
            if data['status'] == 'SUCCESS':
                self.ip_address = data['ip']
                self.mac_address = data['mac']
                self.connected = True
                
                print("\n" + "=" * 60)
                print(f"✅ {self.node_id} connecté au Cloud Network")
                print("=" * 60)
                print(f"🌐 Adresse IP assignée:  {self.ip_address}")
                print(f"🔧 Adresse MAC assignée: {self.mac_address}")
                print("-" * 60)
                print(f"💻 CPU:       {self.cpu} vCPUs")
                print(f"🧠 Mémoire:   {self.memory} GB")
                print(f"💾 Storage:   {self.storage} GB")
                print(f"📶 Bande:     {self.bandwidth} Mbps")
                print("=" * 60)
                print("\nCommandes disponibles:")
                print("  list    - Afficher tous les nœuds")
                print("  send    - Envoyer un fichier")
                print("  exit    - Déconnecter\n")
                
                return True
            else:
                print(f"[ERREUR] {data.get('message', 'Échec de connexion')}")
                return False
                
        except ConnectionRefusedError:
            print(f"[ERREUR] Impossible de se connecter au cloud sur {self.cloud_host}:{self.cloud_port}")
            print("Assurez-vous que cloud_network.py est en cours d'exécution.")
            return False
        except Exception as e:
            print(f"[ERREUR] {e}")
            return False
    
    def list_nodes(self):
        """Liste tous les nœuds du réseau"""
        try:
            request = {'type': 'LIST_NODES'}
            self.socket.send(json.dumps(request).encode('utf-8'))
            
            response = self.socket.recv(4096).decode('utf-8')
            data = json.loads(response)
            
            if data['status'] == 'SUCCESS':
                print("\n" + "=" * 80)
                print("📋 NŒUDS CONNECTÉS AU RÉSEAU")
                print("=" * 80)
                print(f"{'ID':<15} {'IP':<18} {'MAC':<20} {'CPU':<8} {'RAM':<8} {'Storage':<10}")
                print("-" * 80)
                
                for node in data['nodes']:
                    print(f"{node['node_id']:<15} {node['ip']:<18} {node['mac']:<20} "
                          f"{node['cpu']:<8} {node['memory']:<8} {node['storage']:<10}")
                print("=" * 80 + "\n")
        except Exception as e:
            print(f"[ERREUR] {e}")
    
    def send_file(self, destination: str, file_name: str, file_size: float):
        """Envoie un fichier à un autre nœud"""
        try:
            request = {
                'type': 'TRANSFER',
                'source': self.node_id,
                'destination': destination,
                'file_name': file_name,
                'file_size': file_size
            }
            
            self.socket.send(json.dumps(request).encode('utf-8'))
            
            response = self.socket.recv(4096).decode('utf-8')
            data = json.loads(response)
            
            if data['status'] == 'SUCCESS':
                print(f"\n✅ Transfert initié: {file_name} → {destination}")
                print(f"   Taille: {file_size} MB\n")
        except Exception as e:
            print(f"[ERREUR] {e}")
    
    def run_interactive(self):
        """Mode interactif pour le nœud"""
        while self.connected:
            try:
                cmd = input(f"{self.node_id}> ").strip().lower()
                
                if cmd == 'list':
                    self.list_nodes()
                    
                elif cmd == 'send':
                    dest = input("  Destination (node_id): ").strip()
                    fname = input("  Nom du fichier: ").strip()
                    fsize = float(input("  Taille (MB): ").strip())
                    self.send_file(dest, fname, fsize)
                    
                elif cmd == 'exit':
                    print(f"[{self.node_id}] Déconnexion...")
                    self.connected = False
                    self.socket.close()
                    break
                    
                elif cmd == 'help':
                    print("\nCommandes:")
                    print("  list  - Lister les nœuds")
                    print("  send  - Envoyer un fichier")
                    print("  exit  - Quitter\n")
                    
                else:
                    print("Commande inconnue. Tapez 'help' pour l'aide.")
                    
            except KeyboardInterrupt:
                print(f"\n[{self.node_id}] Déconnexion...")
                self.connected = False
                self.socket.close()
                break
            except Exception as e:
                print(f"[ERREUR] {e}")

def main():
    parser = argparse.ArgumentParser(description='Storage Node Client')
    parser.add_argument('node_id', help='Identifiant unique du nœud (ex: node1)')
    parser.add_argument('--cpu', type=int, default=4, help='Nombre de vCPUs (défaut: 4)')
    parser.add_argument('--memory', type=int, default=16, help='Mémoire en GB (défaut: 16)')
    parser.add_argument('--storage', type=int, default=3000, help='Storage en GB (défaut: 3000)')
    parser.add_argument('--bandwidth', type=int, default=1000, help='Bande passante en Mbps (défaut: 1000)')
    parser.add_argument('--host', default='localhost', help='Adresse du cloud (défaut: localhost)')
    parser.add_argument('--port', type=int, default=5000, help='Port du cloud (défaut: 5000)')
    
    args = parser.parse_args()
    
    node = StorageNode(
        node_id=args.node_id,
        cpu=args.cpu,
        memory=args.memory,
        storage=args.storage,
        bandwidth=args.bandwidth,
        cloud_host=args.host,
        cloud_port=args.port
    )
    
    if node.connect_to_cloud():
        node.run_interactive()

if __name__ == "__main__":
    main()
