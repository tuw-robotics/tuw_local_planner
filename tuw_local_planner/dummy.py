import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class Dummy(Node):

    def __init__(self):
        super().__init__('dummy_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            'base_scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def listener_callback(self, msg):
        
        self.get_logger().info('I heard %f' % msg.ranges[0])
        msg = Twist()
        msg.linear.x = 0.1
        self.publisher_.publish(msg)
        
        
        
    def timer_callback(self):
        msg = Twist()
        #msg.linear.x = 0.1
        #self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    dummy = Dummy()

    rclpy.spin(dummy)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    dummy.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
