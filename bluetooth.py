import serial

class Bluetooth():

    ser = None

    def __init__(self, COM, baudrate):
        self.COM = COM
        self.baudrate = baudrate

        self.ser = serial.Serial(port=COM, baudrate=baudrate)

    def send(self, line):
        value = bytearray(line, "utf-8")
        print(line)
        self.ser.write(value)
        
    