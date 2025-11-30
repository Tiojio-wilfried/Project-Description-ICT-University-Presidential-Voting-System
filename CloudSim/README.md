# CloudSim - Simulateur de Réseau Cloud

## 🎬 DÉMARRAGE RAPIDE (3 secondes)

**Option 1 : Lancement automatique (Windows)**
```cmd
start.bat
```
→ Ouvre 4 terminaux automatiquement (cloud + 3 nœuds)

**Option 2 : Démonstration guidée**
```powershell
python demo.py
```
→ Explications étape par étape

**Option 3 : Manuel (ci-dessous)**

---

## 🚀 Démarrage Manuel

### Étape 1 : Lancer le Cloud Network (Terminal 1)
```powershell
python cloud_network.py
```
Vous verrez :
```
🌩️  CLOUD NETWORK SIMULATOR
Serveur démarré sur localhost:5000
En attente de connexions des nœuds...
```

### Étape 2 : Connecter des Nœuds (Terminaux séparés)

**Terminal 2 - Node 1:**
```powershell
python node_client.py node1 --cpu 8 --memory 32 --storage 3000 --bandwidth 1000
```

**Terminal 3 - Node 2:**
```powershell
python node_client.py node2 --cpu 16 --memory 64 --storage 4000 --bandwidth 2000
```

**Terminal 4 - Node 3:**
```powershell
python node_client.py node3 --cpu 8 --memory 32 --storage 3000 --bandwidth 1000
```

## 📋 Fonctionnalités

### Attribution Automatique
Quand un nœud se connecte au cloud :
- ✅ **IP automatique** : 192.168.1.x
- ✅ **MAC automatique** : 00:16:3e:xx:xx:xx
- ✅ Notification au réseau
- ✅ Enregistrement dans le cloud

### Commandes Disponibles (dans chaque nœud)

**`list`** - Afficher tous les nœuds connectés
```
node1> list
📋 NŒUDS CONNECTÉS AU RÉSEAU
ID              IP                 MAC                  CPU      RAM      Storage
node1           192.168.1.1        00:16:3e:45:2a:1f    8        32       3000
node2           192.168.1.2        00:16:3e:7b:c3:89    16       64       4000
```

**`send`** - Envoyer un fichier à un autre nœud
```
node1> send
  Destination (node_id): node2
  Nom du fichier: backup.zip
  Taille (MB): 500
✅ Transfert initié: backup.zip → node2
```

**`exit`** - Déconnecter le nœud

## 🏗️ Architecture

```
Terminal 1          Terminal 2          Terminal 3          Terminal 4
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CLOUD     │◄────┤   NODE 1    │     │   NODE 2    │     │   NODE 3    │
│  NETWORK    │◄────┤ 192.168.1.1 │     │ 192.168.1.2 │     │ 192.168.1.3 │
│ (Serveur)   │◄────┤ MAC: xx:xx  │     │ MAC: yy:yy  │     │ MAC: zz:zz  │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

## 📝 Exemple d'Utilisation Complète

### 1. Démarrer le cloud
```powershell
# Terminal 1
python cloud_network.py
```

### 2. Connecter 3 nœuds (3 terminaux différents)
```powershell
# Terminal 2
python node_client.py node1

# Terminal 3
python node_client.py node2

# Terminal 4
python node_client.py node3
```

### 3. Lister les nœuds (depuis n'importe quel terminal de nœud)
```
node1> list
```

### 4. Transférer un fichier
```
node1> send
  Destination: node3
  Nom: dataset.iso
  Taille: 500
```

## 📸 RÉSULTATS RÉELS

### Serveur Cloud (Terminal 1)
```
============================================================
🌩️  CLOUD NETWORK SIMULATOR
============================================================
Serveur démarré sur localhost:5000
En attente de connexions des nœuds...
Appuyez sur Ctrl+C pour arrêter

[CONNEXION] Nouvelle connexion depuis ('127.0.0.1', 47327)
[ENREGISTREMENT] node1
  ├─ IP: 192.168.1.1
  ├─ MAC: 00:16:3e:04:6f:46
  ├─ CPU: 8 vCPUs
  ├─ RAM: 32 GB
  ├─ Storage: 3000 GB
  └─ Bandwidth: 1000 Mbps
[RÉSEAU] 1 nœud(s) connecté(s)

[CONNEXION] Nouvelle connexion depuis ('127.0.0.1', 47389)
[ENREGISTREMENT] node2
  ├─ IP: 192.168.1.2
  ├─ MAC: 00:16:3e:1a:bf:5e
  ├─ CPU: 16 vCPUs
  ├─ RAM: 64 GB
  ├─ Storage: 4000 GB
  └─ Bandwidth: 2000 Mbps
[RÉSEAU] 2 nœud(s) connecté(s)
```

### Node 1 (Terminal 2)
```
============================================================
✅ node1 connecté au Cloud Network
============================================================
🌐 Adresse IP assignée:  192.168.1.1
🔧 Adresse MAC assignée: 00:16:3e:04:6f:46
------------------------------------------------------------
💻 CPU:       8 vCPUs
🧠 Mémoire:   32 GB
💾 Storage:   3000 GB
📶 Bande:     1000 Mbps
============================================================

Commandes disponibles:
  list    - Afficher tous les nœuds
  send    - Envoyer un fichier
  exit    - Déconnecter

node1> list
============================================================
📋 NŒUDS CONNECTÉS AU RÉSEAU
============================================================
ID              IP                 MAC                  CPU      RAM      Storage
--------------------------------------------------------------------------------
node1           192.168.1.1        00:16:3e:04:6f:46    8        32       3000
node2           192.168.1.2        00:16:3e:1a:bf:5e    16       64       4000
============================================================

node1> send
  Destination (node_id): node2
  Nom du fichier: backup.zip
  Taille (MB): 500

✅ Transfert initié: backup.zip → node2
   Taille: 500 MB

node1> exit
[node1] Déconnexion...
```

---

## 🎯 Ce qui est implémenté

✅ Serveur cloud central qui écoute les connexions  
✅ Attribution automatique d'IP (192.168.1.x)  
✅ Attribution automatique de MAC (00:16:3e:xx:xx:xx)  
✅ Notification automatique au réseau lors de la connexion  
✅ Chaque nœud dans son propre terminal  
✅ Commandes interactives (list, send, exit)  
✅ Support multi-threading pour plusieurs nœuds simultanés  

## 🔧 Options Avancées

Personnaliser un nœud :
```powershell
python node_client.py mynode --cpu 32 --memory 128 --storage 10000 --bandwidth 10000
```

Se connecter à un cloud distant :
```powershell
python node_client.py node1 --host 192.168.0.100 --port 5000
```
