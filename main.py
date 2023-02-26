from app import *

CANVAS_SIZE = "400x400"
CANVAS_COLOR = "black"
CANVAS_TIME_RESOLUTION = 0.01

SOCK_HOST = "127.0.0.1"  # The server's hostname or IP address
SOCK_PORT = 65432  # The port used by the serveri

BT_DEBUG = True
BT_COM = "COM10"
BT_BAUDRATE = 9600
BT_DELAY = 0.1

BOT_CIRCUMFERENCE = 208.916
BOT_STEPS_360 = 200

if __name__ == "__main__":
    app = App(CANVAS_SIZE, CANVAS_COLOR, CANVAS_TIME_RESOLUTION)