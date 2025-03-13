import sys

from more_interfaces.srv import Addnumbers
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(Addnumbers, 'ej3_ex1')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Addnumbers.Request()

    def send_request(self, th1, th2, th3, th4, thitas):
        self.req.th1 = th1
        self.req.th2 = th2
        self.req.th3 = th3
        self.req.th4 = th4
        self.req.thitas = thitas
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
 
    
    future = minimal_client.send_request(float(sys.argv[1]), float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),[float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])])
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    thitas = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]

    minimal_client.get_logger().info(
        'Valores enviados: Thita1: %f ; Thita2: %f ; Thita3: %f ; Thita4: %f) = x:%f ; y:%f ; z:%f ; yaw:%f ; pitch: %f ; roll:%f' %
        (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]), response.x, response.y, response.z, response.yaw,response.pitch, response.roll))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()