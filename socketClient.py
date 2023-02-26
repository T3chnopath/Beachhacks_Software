# echo-client.py
from multiprocessing import Process
import socket
import time

class Client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self, HOST, PORT):
        self.sock.connect((HOST, PORT))

    def sendToServer(self, shapes):
        print("in send to Serveer") 
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

    def inc_forever(self):
        while True:
            time.sleep(1)

    def receive(self):
        p1 = Process(target=self.sock.recv, args=(1024))
        p1.join(timeout=1)
        print(p1)

   