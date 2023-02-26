
import socket               # Import socket module
from threading import Thread
import threading

HOST = "127.0.0.1" # Get local machine name
PORT = 65432                # Reserve a port for your service.

class Server():
    clients = set()
    clients_lock = threading.Lock()
    server = socket.socket()
    HOST = None
    PORT = None

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.server.bind((host, port))
        self.server.listen(5) 

    def handler(self, client, address):
        with self.clients_lock:
            self.clients.add(client)
            
        try:   
            while True:
                data = client.recv(1024)
                
                if not data:
                    break

                else:
                    print(data)
                    
        finally:
            with self.clients_lock:
                self.clients.remove(client)
    
    def getServer(self):
        return self.server

if __name__ == "__main__":
    
    server = Server(HOST, PORT)
    thread = []
    while True:
        host, port = server.getServer().accept()
        Thread(target=server.handler, args = (host,port)).start()
    
    server.getServer().close()

