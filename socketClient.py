# echo-client.py

import socket

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def sendToServer(self, shapes):

        for shape in shapes:
            for lines in shape.getVectors():
                message = ["[" + str(lines.angle), str(lines.magnitude) + "],"] 
                byteMessage = bytes((', '.join(message)), "utf-8")
                self.sock.send(byteMessage)



   