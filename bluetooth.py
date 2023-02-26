class Bluetooth():

    def __init__(self):
        pass

    def send(self, shapes):
        for shape in shapes:
            print("Shape!")
            for lines in shape.getVectors():
                print(lines.angle, lines.magnitude)