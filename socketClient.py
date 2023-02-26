import socket
from bluetooth import *
from main import * 

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def receive(self):
        return(self.sock.recv(1024))

client = Client(SOCK_HOST, SOCK_PORT)
bluetooth = Bluetooth(BT_COM, BT_BAUDRATE, BT_DELAY)

while True:
    for line in str(client.receive()).split():
        bluetooth.send(line)