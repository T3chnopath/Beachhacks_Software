# echo-client.py
import socket

SOCK_HOSTB = "192.168.43.128"
SOCK_PORTB = 65432

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def receive(self):
        return(self.sock.recv(1024))

client = Client(SOCK_HOSTB, SOCK_PORTB)

while True:
    for line in str(client.receive()).split():
        print(line)