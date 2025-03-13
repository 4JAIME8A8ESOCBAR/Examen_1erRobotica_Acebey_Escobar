import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class Sensor1(Node):
    def __init__(self):
        super().__init__('sensor_2')
        self.publisher_ = self.create_publisher(Float64, 's2', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)

    def publish_sensor_data(self):
        value = random.uniform(0.0, 10.0)
        msg = Float64()
        msg.data = value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sensor 2: {value:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = Sensor1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()