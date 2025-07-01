import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import sys

class TestPublisherNode(Node):
    def __init__(self):
        super().__init__("its_publisher_node")
        self.get_logger().info("Node has been started")
        self.publisher_ = self.create_publisher(
            msg_type=String,
            topic='pub_topic', 
            qos_profile=10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.get_logger().info("<ROS2> it's working")
        msg = String()
        msg.data = 'Hi from publisher node _its working_: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing message: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    if args is None:
        args = sys.argv
        
    rclpy.init(args=args)
    node = TestPublisherNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

