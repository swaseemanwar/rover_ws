import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class SerialCmdNode(Node):
    def __init__(self):
        super().__init__('serial_cmd_node')

        # 🔌 Change if needed
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

        self.sub = self.create_subscription(
            String,
            '/rover_cmd',
            self.callback,
            10
        )

        self.get_logger().info("Serial Command Node Started")

    def callback(self, msg):
        cmd = msg.data.strip().upper()

        if cmd in ['F', 'B', 'L', 'R', 'S']:
            self.ser.write(cmd.encode())
            self.get_logger().info(f"Sent: {cmd}")
        else:
            self.get_logger().warn(f"Invalid: {cmd}")


def main(args=None):
    rclpy.init(args=args)
    node = SerialCmdNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
