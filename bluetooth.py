import serial

class Bluetooth():

    ser = None

    def __init__(self, COM, baudrate):
        self.COM = COM
        self.baudrate = baudrate

        self.ser = serial.Serial(port=COM, baudrate=baudrate)

    def send(self, shapes):
        for shape in shapes:
            for lines in shape.getVectors():
                print(lines.angle, lines.magnitude)
                self.ser.write("test!")

    