from app import *

CANVAS_SIZE = "400x400"
CANVAS_COLOR = "black"

SOCK_HOST = "127.0.0.1"  # The server's hostname or IP address
SOCK_PORT = 65432  # The port used by the server

if __name__ == "__main__":
    App(CANVAS_SIZE, CANVAS_COLOR, SOCK_HOST, SOCK_PORT)