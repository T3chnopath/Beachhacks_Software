
import socket               # Import socket module
import time

from main import *

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

    def sendToClient(self, shapes):
        finalMessage = []
        for x in range(0, len(shapes)):
            firstFlag = 1
            message = []
            for lines in shapes[x].getVectors():

                if firstFlag or lines == shapes[x].getVectors()[-1]:
                    temp = "[0, " + str(round(lines.angle, 3)), str(round(lines.magnitude, 3)) + "]"
                    message.append(", ".join(temp))
                    firstFlag = 0

                else:
                    temp = "[1 , " + str(round(lines.angle, 3)), str(round(lines.magnitude, 3)) + "]"
                    message.append(", ".join(temp))
                    lastAngle = lines.angle

                #lift pen 
                temp = "[0, " + str(round(lastAngle, 3)), str(0) + "]"
                message.append(", ".join(temp))
            

        byteMessage = bytes((''.join(message)), "utf-8")
        self.conn.sendall(byteMessage)

