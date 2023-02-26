import socket
from bluetooth import *

SOCK_HOSTB = "192.168.43.128"
SOCK_PORTB = 65432

BT_COM = "COM10"
BT_BAUDRATE = 9600

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def receive(self):
        return(self.sock.recv(1024))

client = Client(SOCK_HOSTB, SOCK_PORTB)
bluetooth = Bluetooth(BT_COM, BT_BAUDRATE)

while True:
    for line in str(client.receive()).split():
        bluetooth.send(line)