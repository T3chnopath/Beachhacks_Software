# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def sendToServer(self, string):
        self.sock.sendall(bytes(string, "utf-8"))
        data = self.sock.recv(1024)
        print(data)

PC1 = Client(HOST, PORT)
PC1.sendToServer("From client!")


   