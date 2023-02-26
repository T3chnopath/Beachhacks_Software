from tkinter import Tk, Canvas, Button
import math
import time
from multiprocessing import Process
from multiprocessing import Value
from socketClientA import * 
from bluetooth import *
class App():
    sock = None

    canvasClear = True
    lineBuf = []
    shapeBuf = None 
    shapes = []
    timeResolution = None
    pollTime = None

    app = None
    canvas = None

    def __init__(self, size, bg, timeResolution, host, port, pollTime):
        
        #initialization
        self.app = Tk()
        self.app.geometry(size)
        
        self.canvas = Canvas(self.app, bg=bg)
        self.canvas.pack(anchor="nw", fill="both", expand=1), 

        #bind left click and mouse motion 
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<ButtonRelease-1>", self.left_unclick)
        self.canvas.bind("<B1-Motion>", self.draw)
        

        #Button to send commands to server
        btnDraw = Button(self.app, text='Send', width=10,
             height=2, bd='10', command=self.send)
        btnDraw.place(x=0, y=340)
    
        btnPoll = Button(self.app, text='Receive', width=10,
             height=2, bd='10', command=self.checkServer)
        btnPoll.place(x=300, y=340)
        


        #set time resolution
        self.timeResolution = timeResolution
        self.sock = Client(host, port)

        #initalize app
        self.pollTime = pollTime
        self.app.mainloop()

    def checkServer(self):
        print("in check server")
        print(self.sock.receive())


    #get position on left click
    def left_click(self, event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    #draw based on mouse motion
    def draw(self, event):
        global lasx, lasy
        self.canvas.create_line((lasx, lasy, event.x, event.y), 
                        fill='red', 
                        width=2)

        #if first point, create offset from bot start coordinate 
        if(self.canvasClear):
            self.createLine([0, 0], [event.x, event.y])
            self.canvasClear = False

        #else, operate based on first and last point 
        else:
            self.createLine([lasx, lasy], [event.x, event.y])   

        #update last x and y variable
        lasx, lasy = event.x, event.y
        
        #update based on bot resolution
        time.sleep(self.timeResolution)

    def createLine(self, last, current):
        #grab offset movement
        lenx = current[0] - last[0]
        leny = current[1] - last[1]
        
        #divison, return 0 if divide by 0
        divison = leny and lenx / leny or 0
        
        #find angle and magnitude 
        angle = math.atan(divison) * 180 / math.pi
        magnitude = math.sqrt(lenx**2 + leny**2)

        #create line 
        self.lineBuf.append(Line(angle, magnitude))


    #enter when 
    def left_unclick(self, event):
        shape = Shape(self.lineBuf)
        self.shapes.append(shape)

    def send(self):
        self.sock.sendToServer(self.shapes)

class Line():
    angle = None    
    magnitude = None

    #initilization
    def __init__(self, angle, magnitude):
        self.angle = angle
        self.magnitude = magnitude

    #getter function
    def angle(self):
        return self.angle

    def magnitude(self):
        return self.magnitude

class Shape():
    _vectors = []

    #initalization
    def __init__(self, lines):
        for x in lines:
            self._vectors.append(x)

    #getter function
    def getVectors(self):
        return self._vectors