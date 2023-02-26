# echo-client.py
import socket
import time
from multiprocessing import Value

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def sendToServer(self, shapes):
        finalMessage = []
        for x in range(0, len(shapes)):
            firstFlag = 1
            message = []
            for lines in shapes[x].getVectors():
                
                if firstFlag:
                    temp = "[0, " + str(round(lines.angle, 3)), str(round(lines.magnitude, 3)) + "]"
                    message.append(", ".join(temp))
                    firstFlag = 0
                else:
                    temp = "[1, " + str(round(lines.angle, 3)), str(round(lines.magnitude, 3)) + "]"
                    message.append(", ".join(temp))

            byteMessage = bytes((''.join(message)), "utf-8")
            self.sock.send(byteMessage)

    def receive(self):
        return(self.sock.recv(1024))

   