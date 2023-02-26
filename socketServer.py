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
import _thread as thread

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print(msg)
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = "127.0.0.1" # Get local machine name
port = 65432                # Reserve a port for your service.

#print 'Server started!'
#print 'Waiting for clients...'

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

#print 'Got connection from', addr
while True:
   c, addr = s.accept()     # Establish connection with client.
   thread.start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()