'''
import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server``:

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data)

class Server:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''

#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket               # Import socket module
from threading import Thread
import threading

clients = set()
clients_lock = threading.Lock()

def on_new_client(client,addr):
    '''
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()
    '''
    with clients_lock:
        clients.add(client)
    try:    
        while True:
            data = client.recv(1024)
            print(data)
            if not data:
                break
            else:
                
                with clients_lock:
                    for c in clients:
                        c.sendall(data)
    finally:
        with clients_lock:
            clients.remove(client)

s = socket.socket()         # Create a socket object
host = "127.0.0.1" # Get local machine name
port = 65432                # Reserve a port for your service.

#print 'Server started!'
#print 'Waiting for clients...'

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

#print 'Got connection from', addr
while True:
   host, port = s.accept()     # Establish connection with client.
   #thread.start_new_thread(on_new_client,(c,addr))
   Thread(target=on_new_client, args = (host,port)).start()
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()