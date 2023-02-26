
import socket               # Import socket module
import time

HOST = "192.168.43.128" # Get local machine name
PORT = 65432                # Reserve a port for your service.

class Server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = None
    PORT = None
    conn = None
    addr = None

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.server.bind((host, port))
        self.server.listen()
        self.conn, self.addr = self.server.accept() 

    def sendToClient(self, data):
        self.conn.sendall(bytes(data, "utf-8"))
    
    def getServer(self):
        return self.server

if __name__ == "__main__":
    
    server = Server(HOST, PORT)
    
    while True:
        server.sendToClient("test")
        time.sleep(1)

