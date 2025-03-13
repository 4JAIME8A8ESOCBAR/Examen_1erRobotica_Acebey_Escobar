from more_interfaces.srv import Addnumbers

import rclpy
from rclpy.node import Node
import sympy as sp

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Addnumbers, 'ej3_ex1', self.calcule_of_kinematic)

    def calcule_of_kinematic(self, request, response):
        l1 = 69.5
        l2 = 71.5

        th1, th2, th3, th4, l1, l2 = sp.symbols('th1 th2 th3 th4 L1 L2')

        Rx1 = sp.Matrix([
            [1, 0, 0, 0],
            [0, sp.cos(th1), -sp.sin(th1), 0],
            [0, sp.sin(th1), sp.cos(th1), 0],
            [0, 0, 0, 1]
        ])
        Ry1 = sp.Matrix([
            [sp.cos(-th2), 0, sp.sin(-th2), 0],
            [0, 1, 0, 0],
            [-sp.sin(-th2), 0, sp.cos(-th2), 0],
            [0, 0, 0, 1]
        ])

        Tz1 = sp.Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, -l1],
            [0, 0, 0, 1]
        ])

        Ry1 = sp.Matrix([
            [sp.cos(-th3), 0, sp.sin(-th3), 0],
            [0, 1, 0, 0],
            [-sp.sin(-th3), 0, sp.cos(-th3), 0],
            [0, 0, 0, 1]
        ])
        Tz2 = sp.Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, -l2],
            [0, 0, 0, 1]
        ])
        Ry3 = sp.Matrix([
            [sp.cos(-th4), 0, sp.sin(-th4), 0],
            [0, 1, 0, 0],
            [-sp.sin(-th4), 0, sp.cos(-th4), 0],
            [0, 0, 0, 1]
        ])

        M = Rx1 * Ry1 * Tz1 * Ry1 * Tz2 * Ry3

        # Simplificar la matriz M multiplicada por el vector [0, 0, 0, 1]
        M_simplified = sp.simplify(M * sp.Matrix([0, 0, 0, 1]))

        # Extraer los valores de x, y, z
        x = M_simplified[0]  # Cambiar de notación de paréntesis a corchetes
        y = M_simplified[1]
        z = M_simplified[2]

        # Sustituir valores numéricos
        M_numeric = M_simplified.subs({
            th1: (request.th1)*0.0175,
            th2: (request.th2)*0.0175,
            th3: (request.th3)*0.0175,
            l1: 69.5,
            l2: 71.5
        })

        # Extraer los valores de x, y, z
        x = M_numeric[0]
        y = M_numeric[1]
        z = M_numeric[2]

        
        response.x = float(x)
        response.y = float(y)
        response.z = float(z)
        response.yaw = float(1.0)
        response.pitch = float(1.0)
        response.roll = float(1.0)

        self.get_logger().info('Request\n x: %f y: %f z: %f ; yaw: %f pitch:%f row: %f' % (request.x, request.y, request.z, request.yaw, request.pitch, request.roll))
        

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()