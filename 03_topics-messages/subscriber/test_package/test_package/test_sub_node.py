import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import sys

class TestSubscriberNode(Node):
    def __init__(self):
        super().__init__("its_subscriber_node")
        self.get_logger().info("Node has been started")
        self.subscription = self.create_subscription(
            msg_type=String,
            topic='pub_topic',
            callback=self.listener_callback,
            qos_profile=10)
        self.subscription  # prevent unused variable warning


    def listener_callback(self, msg: String):
        self.get_logger().info("<ROS2> it's working and listenning to the topic %s" % msg.data)

def main(args=None):
    if args is None:
        args = sys.argv
        
    rclpy.init(args=args)
    node = TestSubscriberNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

