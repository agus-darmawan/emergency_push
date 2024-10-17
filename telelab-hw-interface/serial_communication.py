import serial
import time

class SerialCommunication:
    def __init__(self, com1_port, com2_port, baudrate=9600):
        self.com1 = serial.Serial(com1_port, baudrate, timeout=1)
        self.com2 = serial.Serial(com2_port, baudrate, timeout=1)

    def send_to_com1(self, data):
        try:
            self.com1.write(data.encode())
        except Exception as e:
            print(f"Failed to send data to COM1: {e}")

    def receive_from_com2(self):
        try:
            time.sleep(1)
            data = self.com2.read_all().decode()
            return data
        except Exception as e:
            print(f"Failed to receive data from COM2: {e}")
            return None
