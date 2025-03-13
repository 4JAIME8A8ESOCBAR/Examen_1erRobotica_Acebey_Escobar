import rclpy
from rclpy.node import Node
from e2_interface.msg import Result

class DisplayNode(Node):
    def __init__(self):
        super().__init__('result_node')
        self.subscription = self.create_subscription(Result,'filtered_sensor',self.listener_callback,10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibido -> {msg.name}: {msg.sensor_value:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = DisplayNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
