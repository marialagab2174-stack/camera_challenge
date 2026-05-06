from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Déclaration des arguments de lancement
    res_arg = DeclareLaunchArgument(
        'resolution',
        default_value='720p',
        description='Résolution de la caméra (ex: 480p, 720p, 1080p)'
    )
    
    fps_arg = DeclareLaunchArgument(
        'fps',
        default_value='30',
        description='Frames par seconde'
    )

    # Configuration du Node avec les LaunchConfiguration
    camera_node = Node(
        package='camera_challenge',
        executable='camera_node',
        name='camera_system',
        parameters=[{
            'resolution': LaunchConfiguration('resolution'),
            'fps': LaunchConfiguration('fps')
        }],
        output='screen'
    )

    return LaunchDescription([
        res_arg,
        fps_arg,
        camera_node
    ])
