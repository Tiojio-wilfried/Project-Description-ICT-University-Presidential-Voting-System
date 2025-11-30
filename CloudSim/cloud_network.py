"""
Cloud Network Server - Gère le réseau virtuel central
Lance ce fichier en premier dans un terminal séparé
"""
import socket
import threading
import json
import random
import time
from typing import Dict, Optional

class CloudNetwork:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.nodes: Dict[str, dict] = {}  # node_id -> {ip, mac, socket, address}
        self.ip_counter = 1
        self.running = True
        self.lock = threading.Lock()
        
    def generate_mac_address(self) -> str:
        """Génère une adresse MAC aléatoire"""
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: f"{x:02x}", mac))
    
    def assign_ip(self) -> str:
        """Attribue une nouvelle adresse IP"""
        ip = f"192.168.1.{self.ip_counter}"
        self.ip_counter += 1
        return ip
    
    def handle_client(self, client_socket, address):
        """Gère la connexion d'un nœud"""
        print(f"[CONNEXION] Nouvelle connexion depuis {address}")
        
        try:
            # Recevoir l'enregistrement du nœud
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                return
                
            request = json.loads(data)
            
            if request['type'] == 'REGISTER':
                node_id = request['node_id']
                node_info = request['node_info']
                
                with self.lock:
                    # Attribuer IP et MAC
                    ip_address = self.assign_ip()
                    mac_address = self.generate_mac_address()
                    
                    self.nodes[node_id] = {
                        'ip': ip_address,
                        'mac': mac_address,
                        'cpu': node_info['cpu'],
                        'memory': node_info['memory'],
                        'storage': node_info['storage'],
                        'bandwidth': node_info['bandwidth'],
                        'socket': client_socket,
                        'address': address
                    }
                    
                    # Envoyer la configuration au nœud
                    response = {
                        'status': 'SUCCESS',
                        'ip': ip_address,
                        'mac': mac_address,
                        'message': f'Nœud {node_id} enregistré avec succès'
                    }
                    
                    client_socket.send(json.dumps(response).encode('utf-8'))
                    
                    print(f"[ENREGISTREMENT] {node_id}")
                    print(f"  ├─ IP: {ip_address}")
                    print(f"  ├─ MAC: {mac_address}")
                    print(f"  ├─ CPU: {node_info['cpu']} vCPUs")
                    print(f"  ├─ RAM: {node_info['memory']} GB")
                    print(f"  ├─ Storage: {node_info['storage']} GB")
                    print(f"  └─ Bandwidth: {node_info['bandwidth']} Mbps")
                    print(f"[RÉSEAU] {len(self.nodes)} nœud(s) connecté(s)\n")
                    
            elif request['type'] == 'LIST_NODES':
                # Retourner la liste des nœuds
                nodes_list = []
                with self.lock:
                    for nid, info in self.nodes.items():
                        nodes_list.append({
                            'node_id': nid,
                            'ip': info['ip'],
                            'mac': info['mac'],
                            'cpu': info['cpu'],
                            'memory': info['memory'],
                            'storage': info['storage']
                        })
                
                response = {
                    'status': 'SUCCESS',
                    'nodes': nodes_list
                }
                client_socket.send(json.dumps(response).encode('utf-8'))
                
            elif request['type'] == 'TRANSFER':
                # Gérer une demande de transfert
                src = request['source']
                dst = request['destination']
                file_name = request['file_name']
                file_size = request['file_size']
                
                print(f"[TRANSFERT] {src} → {dst}: {file_name} ({file_size} MB)")
                
                response = {
                    'status': 'SUCCESS',
                    'message': 'Transfert initié'
                }
                client_socket.send(json.dumps(response).encode('utf-8'))
                
        except Exception as e:
            print(f"[ERREUR] {e}")
        finally:
            # Garder la connexion ouverte pour les nœuds enregistrés
            pass
    
    def start(self):
        """Démarre le serveur cloud"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen()
        
        print("=" * 60)
        print("🌩️  CLOUD NETWORK SIMULATOR")
        print("=" * 60)
        print(f"Serveur démarré sur {self.host}:{self.port}")
        print("En attente de connexions des nœuds...")
        print("Appuyez sur Ctrl+C pour arrêter\n")
        
        try:
            while self.running:
                client, address = server.accept()
                thread = threading.Thread(target=self.handle_client, args=(client, address))
                thread.daemon = True
                thread.start()
        except KeyboardInterrupt:
            print("\n\n[ARRÊT] Fermeture du serveur...")
            self.running = False
            server.close()
            print("[OK] Serveur arrêté")

if __name__ == "__main__":
    cloud = CloudNetwork()
    cloud.start()
