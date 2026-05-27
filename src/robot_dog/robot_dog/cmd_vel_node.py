import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelNode(Node):

    def __init__(self):
        super().__init__('cmd_vel_node')
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

    def cmd_vel_callback(self, msg):
        self.linear_x = msg.linear.x
        self.angular_z = msg.angular.z
        self.get_logger().info(f'Instructions Received: linear.x={self.linear_x}, angular.z={self.angular_z}')

def main(args = None):
    rclpy.init(args=args)   # Starts ROS2
    node = CmdVelNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
