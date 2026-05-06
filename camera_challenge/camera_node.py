import rclpy
from rclpy.node import Node

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        # Déclaration des paramètres ROS 2
        self.declare_parameter('resolution', '720p')
        self.declare_parameter('fps', 30)

        res = self.get_parameter('resolution').get_parameter_value().string_value
        fps = self.get_parameter('fps').get_parameter_value().integer_value

        self.get_logger().info(f'Caméra démarrée avec la résolution : {res} et {fps} FPS')

def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
