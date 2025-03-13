import rclpy
from rclpy.node import Node 

#importar el tipo de mesnaje con el cual el node va a crear
from std_msgs.msg import Int32MultiArray # Se importan tipo s de mensajes "String"
#para umportat cada node siempre va a aestar enscpsulado 
#siempre cuadno se crea el node se cra lo siguiente en si:
class MiNodoPublicador(Node):
    def __init__(self):
        super().__init__('Nodo_Pub')
        self.publisher = self.create_publisher(Int32MultiArray, 'ex1', 10)  # creacion del Topico (qt_size)
        time_period = 3 # definir el tiempo de publicar 
        self.timer = self.create_timer(time_period, self.timer_callback)# instancia del tiempo en que se publicar a el timer
        self.i = 0
        self.sensors = []

    def timer_callback(self):
        msg = Int32MultiArray()
        self.sensors = [(self.i >> ii) & 1 for ii in range(2, -1, -1)]

        msg.data = self.sensors

        self.publisher.publish(msg)
        self.get_logger().info('Publicado: "%s"' % msg.data)
        self.i +=1
        if self.i == 8:
            self.i = 0

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoPublicador() # se instancia toda la abtraccionde al nodo 
    rclpy.spin(mi_nodo)  # Hace que Corra para siempre es infinito a menos de una iterrupcion por teclado
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



