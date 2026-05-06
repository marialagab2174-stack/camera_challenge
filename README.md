# Challenge : Camera Launch Configuration 📸

Ce projet démontre l'utilisation des **Launch Files** ROS 2 pour passer des paramètres dynamiques à un nœud sans modifier le code source.

## 🎯 Objectifs
- Utiliser `DeclareLaunchArgument` pour définir des options (`resolution`, `fps`).
- Utiliser `LaunchConfiguration` pour injecter ces valeurs dans le nœud.
- Configurer le `setup.py` pour exporter le dossier launch.

## 🚀 Installation
```bash
cd ~/ros2_ws
colcon build --packages-select camera_challenge
source install/setup.bash
```

## 🛠 Utilisation
Lancer avec la configuration par défaut (720p, 30 FPS) :
```bash
ros2 launch camera_challenge camera_launch.py
```

Lancer avec des paramètres personnalisés (1080p, 60 FPS) :
```bash
ros2 launch camera_challenge camera_launch.py resolution:="1080p" fps:=60
```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent
