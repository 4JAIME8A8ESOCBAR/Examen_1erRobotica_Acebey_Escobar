import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from e2_interface.msg import Result


class FilterNode(Node):
    def __init__(self):
        super().__init__('filter_node')
        self.subscription_1 = self.create_subscription(Float64, 's1', self.sensor_callback_1, 10)
        self.subscription_2 = self.create_subscription(Float64, 's2', self.sensor_callback_2, 10)
        self.subscription_3 = self.create_subscription(Float64, 's3', self.sensor_callback_3, 10)
        
        self.publisher_ = self.create_publisher(Result, 'filtered_sensor', 10)
        self.timer = self.create_timer(1.0, self.publish_filtered_data)

        self.sensor_values = {'sensor_1': None, 'sensor_2': None, 'sensor_3': None}

    def sensor_callback_1(self, msg):
        self.sensor_values['sensor_1'] = msg.data

    def sensor_callback_2(self, msg):
        self.sensor_values['sensor_2'] = msg.data

    def sensor_callback_3(self, msg):
        self.sensor_values['sensor_3'] = msg.data

    def publish_filtered_data(self):
        if None not in self.sensor_values.values():
            avg_value = sum(self.sensor_values.values()) / 3.0
            msg = Result()
            msg.sensor_value = avg_value
            msg.name = "Promedio de Sensores"
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publicando Promedio: {avg_value:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = FilterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
