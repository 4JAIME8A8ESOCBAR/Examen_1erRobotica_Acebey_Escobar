import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

class MiSubscriptor(Node):
    def __init__(self):
        super().__init__('Nodo_Subscriptor')
        self.subscription = self.create_subscription(Int32MultiArray, 'ex1', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.sensors = msg.data
        self.si = self.sensors[0]
        self.sc = self.sensors[1]
        self.sd = self.sensors[2]
            
        self.sinot = 1 - self.si
        self.scnot = 1 - self.sc 
        self.sdnot = 1 - self.sd

        self.mi1 = self.scnot  & self.sdnot
        self.mi2 = self.si  & self.scnot
        self.mi3 = self.mi2  & self.sd

        self.mi4 = self.si  & self.sc
        self.mi5 = self.mi4  & self.sdnot
        self.mi = self.mi1 | self.mi3 | self.mi5
        
        self.md1 = self.scnot  & self.sd
        self.md2 = self.sinot & self.scnot
        self.md3 = self.md2 & self.sdnot

        self.md4 = self.sinot & self.sc
        self.md5 = self.md4 & self.sd
        self.md = self.md1 | self.md3 | self.md5

        #self.get_logger().info('Recived: "%s"' % self.sensors[0])
        #self.get_logger().info('Value Motors: MI:"%f" ; MD:"%f"; Estado: Alto' % (self.mi, self.md))
        if self.mi==0 and self.md==0:
            self.get_logger().info('Value Motors: MI:%f , MD:%f Estado: Alto' % (self.mi, self.md))
        elif self.mi==0 and self.md==1:
            self.get_logger().info('Value Motors: MI:%f , MD:%f Estado: Derecha' % (self.mi, self.md))
        elif self.mi==1 and self.md==0:
            self.get_logger().info('Value Motors: MI:%f , MD:%f Estado: Izquierda' % (self.mi, self.md))
        else:
            self.get_logger().info('Value Motors: MI:%f , MD:%f Estado: Adelante' % (self.mi, self.md))

        

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiSubscriptor()
    rclpy.spin(mi_nodo)
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()