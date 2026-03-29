import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import termios
import tty
import select

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control')

        self.publisher = self.create_publisher(String, '/rover_cmd', 10)

        self.get_logger().info("""
W/S → Forward/Backward
A/D → Left/Right
SPACE → Stop
CTRL+C → Exit
""")

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def run(self):
        while rclpy.ok():
            key = self.get_key()

            msg = String()

            if key == 'w':
                msg.data = 'F'
            elif key == 's':
                msg.data = 'B'
            elif key == 'a':
                msg.data = 'L'
            elif key == 'd':
                msg.data = 'R'
            elif key == ' ':
                msg.data = 'S'
            else:
                msg.data = 'S'  # 🔴 STOP when no key pressed

            self.publisher.publish(msg)


def main(args=None):
    global settings
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init(args=args)
    node = KeyboardControl()

    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()
