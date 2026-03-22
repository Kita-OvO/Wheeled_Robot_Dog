import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class PubImuNode(Node):

    def __init__(self):
        super().__init__("pub_imu_node")
        self.publisher = self.create_publisher(Imu, '/imu/data', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
    
    def timer_callback(self):
        msg = Imu()
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PubImuNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
