"""
Script de démonstration automatique du CloudSim
Montre comment utiliser le système complet
"""
import subprocess
import time
import sys

def print_section(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")

def main():
    print_section("🌩️  DÉMONSTRATION CloudSim")
    
    print("Ce script va vous montrer comment utiliser CloudSim en 3 étapes:\n")
    print("1️⃣  Démarrer le Cloud Network (serveur central)")
    print("2️⃣  Connecter des nœuds (chacun dans son terminal)")
    print("3️⃣  Utiliser les commandes (list, send)\n")
    
    input("Appuyez sur Entrée pour commencer...")
    
    # Étape 1
    print_section("ÉTAPE 1: Démarrer le Cloud Network")
    print("📝 Dans un NOUVEAU terminal, exécutez:")
    print("\n    python cloud_network.py\n")
    print("Vous verrez:")
    print("    🌩️  CLOUD NETWORK SIMULATOR")
    print("    Serveur démarré sur localhost:5000")
    print("    En attente de connexions...\n")
    
    input("✅ Avez-vous démarré cloud_network.py ? (Entrée pour continuer)")
    
    # Étape 2
    print_section("ÉTAPE 2: Connecter des Nœuds")
    print("📝 Dans d'AUTRES terminaux (un par nœud), exécutez:\n")
    
    print("Terminal 2 (Node1):")
    print("    python node_client.py node1 --cpu 8 --memory 32 --storage 3000\n")
    
    print("Terminal 3 (Node2):")
    print("    python node_client.py node2 --cpu 16 --memory 64 --storage 4000\n")
    
    print("Terminal 4 (Node3):")
    print("    python node_client.py node3\n")
    
    print("Chaque nœud recevra automatiquement:")
    print("    ✓ Adresse IP (192.168.1.x)")
    print("    ✓ Adresse MAC (00:16:3e:xx:xx:xx)\n")
    
    input("✅ Avez-vous connecté au moins 2 nœuds ? (Entrée pour continuer)")
    
    # Étape 3
    print_section("ÉTAPE 3: Utiliser les Commandes")
    print("Dans N'IMPORTE QUEL terminal de nœud, tapez:\n")
    
    print("📋 Lister tous les nœuds:")
    print("    node1> list\n")
    print("    Résultat:")
    print("    ┌───────────┬─────────────┬──────────────────┬─────┬─────┬─────────┐")
    print("    │ ID        │ IP          │ MAC              │ CPU │ RAM │ Storage │")
    print("    ├───────────┼─────────────┼──────────────────┼─────┼─────┼─────────┤")
    print("    │ node1     │ 192.168.1.1 │ 00:16:3e:xx:xx   │ 8   │ 32  │ 3000    │")
    print("    │ node2     │ 192.168.1.2 │ 00:16:3e:yy:yy   │ 16  │ 64  │ 4000    │")
    print("    └───────────┴─────────────┴──────────────────┴─────┴─────┴─────────┘\n")
    
    print("📤 Envoyer un fichier:")
    print("    node1> send")
    print("      Destination (node_id): node2")
    print("      Nom du fichier: backup.zip")
    print("      Taille (MB): 500\n")
    print("    ✅ Transfert initié: backup.zip → node2\n")
    
    print("🚪 Déconnecter:")
    print("    node1> exit\n")
    
    print_section("✨ ARCHITECTURE DU SYSTÈME")
    print("""
    Terminal 1            Terminal 2           Terminal 3           Terminal 4
    ┌──────────────┐     ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
    │   CLOUD      │◄────┤   NODE 1     │    │   NODE 2     │    │   NODE 3     │
    │   NETWORK    │◄────┤ 192.168.1.1  │    │ 192.168.1.2  │    │ 192.168.1.3  │
    │  (Serveur)   │◄────┤ 00:16:3e:... │    │ 00:16:3e:... │    │ 00:16:3e:... │
    └──────────────┘     └──────────────┘    └──────────────┘    └──────────────┘
         PORT 5000
    """)
    
    print_section("📚 RÉSUMÉ DES COMMANDES")
    print("Démarrer le cloud:")
    print("    python cloud_network.py\n")
    
    print("Connecter un nœud:")
    print("    python node_client.py <node_id> [options]\n")
    
    print("Options disponibles:")
    print("    --cpu <n>        Nombre de vCPUs (défaut: 4)")
    print("    --memory <n>     Mémoire en GB (défaut: 16)")
    print("    --storage <n>    Stockage en GB (défaut: 3000)")
    print("    --bandwidth <n>  Bande passante en Mbps (défaut: 1000)\n")
    
    print("Commandes interactives (dans un nœud):")
    print("    list    - Lister tous les nœuds")
    print("    send    - Envoyer un fichier")
    print("    exit    - Déconnecter\n")
    
    print_section("🎯 FONCTIONNALITÉS IMPLÉMENTÉES")
    print("✅ Attribution automatique d'IP (192.168.1.x)")
    print("✅ Attribution automatique de MAC (00:16:3e:xx:xx:xx)")
    print("✅ Notification au cloud lors de la connexion")
    print("✅ Architecture multi-terminaux (cloud + nœuds)")
    print("✅ Communication par sockets TCP")
    print("✅ Commandes interactives (list, send, exit)")
    print("✅ Support de plusieurs nœuds simultanés\n")
    
    print("=" * 70)
    print("  Démonstration terminée ! Essayez maintenant par vous-même.")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
