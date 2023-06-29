import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('first node')
        self.create_timer(1.0, self.timer_callback) # a timer that runs the callback func every 1 sec

    def timer_callback(self):
        self.get_logger().info('Hello') # logging with ros2

def main(args=None):
    rclpy.init(args=args) # Initialize ros2 communications
    node = MyNode()
    rclpy.spin(node) # run the node infinitely until kill command is given
    rclpy.shutdown() # Shutdown the node and close all ros2 communications

if __name__ == '__main__':
    main()
