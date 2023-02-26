# echo-client.py

import socket

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def sendToServer(self, shapes):
        
        for x in range(0, len(shapes)):
            firstFlag = 1
            for lines in shapes[x].getVectors():

                if firstFlag:
                    message = ["[0, " + str(lines.angle), str(lines.magnitude) + "],"] 
                    firstFlag = 0
                else:
                    message = ["[1, " + str(lines.angle), str(lines.magnitude) + "],"] 
                    
                byteMessage = bytes((', '.join(message)), "utf-8")
                self.sock.send(byteMessage)

    def recive(self):
        data = self.sock.recv(1024)
        return(data)


   