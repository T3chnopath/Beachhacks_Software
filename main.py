from app import *

CANVAS_SIZE = "400x400"
CANVAS_COLOR = "black"
CANVAS_TIME_RESOLUTION = 0.05

SOCK_HOSTA = "192.168.43.128"  # The server's hostname or IP address
SOCK_PORTA = 65432  # The port used by the server

SOCK_HOSTB = "192.168.43.128"
SOCK_PORTB = 65432

POLL_TIME = 1000

if __name__ == "__main__":
    App(CANVAS_SIZE, CANVAS_COLOR, CANVAS_TIME_RESOLUTION, \
        SOCK_HOSTA, SOCK_PORTA, POLL_TIME)