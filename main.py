from app import *

CANVAS_SIZE = "400x400"
CANVAS_COLOR = "black"
CANVAS_TIME_RESOLUTION = 0.05

SOCK_HOST = "192.168.43.128"  # The server's hostname or IP address
SOCK_PORT = 65432  # The port used by the server

POLL_TIME = 3000

if __name__ == "__main__":
    App(CANVAS_SIZE, CANVAS_COLOR, CANVAS_TIME_RESOLUTION, \
        SOCK_HOST, SOCK_PORT, POLL_TIME)