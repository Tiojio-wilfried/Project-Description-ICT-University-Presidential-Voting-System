@echo off
REM Script de lancement rapide pour CloudSim
echo ========================================
echo   CloudSim - Demarrage Rapide
echo ========================================
echo.
echo Ce script va ouvrir 4 fenetres:
echo   1. Cloud Network (serveur)
echo   2. Node 1
echo   3. Node 2
echo   4. Node 3
echo.
pause

REM Démarrer le cloud
start "Cloud Network" cmd /k "python cloud_network.py"
timeout /t 2 /nobreak >nul

REM Démarrer les nœuds
start "Node 1" cmd /k "python node_client.py node1 --cpu 8 --memory 32 --storage 3000"
timeout /t 1 /nobreak >nul

start "Node 2" cmd /k "python node_client.py node2 --cpu 16 --memory 64 --storage 4000"
timeout /t 1 /nobreak >nul

start "Node 3" cmd /k "python node_client.py node3 --cpu 8 --memory 32 --storage 3000"

echo.
echo ========================================
echo   4 terminaux ont ete ouverts !
echo ========================================
echo.
echo Dans chaque terminal de noeud, vous pouvez:
echo   - Taper "list" pour voir tous les noeuds
echo   - Taper "send" pour envoyer un fichier
echo   - Taper "exit" pour deconnecter
echo.
pause
