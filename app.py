from tkinter import Tk, Canvas, Button
import math
import time
from socketServer import * 
from bluetooth import *

class App():
    sock = None

    canvasClear = True
    lineBuf = []
    shapeBuf = None 
    shapes = []
    timeResolution = None

    app = None
    canvas = None

    def __init__(self, size, bg, timeResolution):
        
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
    
        #set time resolution
        self.timeResolution = timeResolution
        self.sock = Server(SOCK_HOST, SOCK_PORT)

        #initalize app
        self.app.mainloop()


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
        if self.canvasClear:
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
        
        #find angle
        #divison = leny and lenx / leny or -1
        angle = math.atan(lenx / leny) * 180 / math.pi
        angle = abs(angle)

        #quadrant 1
        if lenx >= 0 and leny < 0:
            theta = angle

        #quadrant 2
        elif lenx <= 0 and leny < 0:
            theta = 360 - angle

        #quadrant 3
        elif lenx <= 0 and leny > 0:
            theta = 180 + angle

        #quadrant 4
        elif lenx >= 0 and leny > 0:
            theta = 180 - angle


        #find magnitude 
        magnitude = math.sqrt(lenx**2 + leny**2)

        #create line buf
        self.lineBuf.append(Line(theta, magnitude))

    #enter when 
    def left_unclick(self, event):
        self.lineBuf.append 
        shape = Shape(self.lineBuf)
        self.shapes.append(shape)

    def send(self):
        self.sock.sendToClient(self.shapes)

class Line():
    angle = None    
    magnitude = None

    #initilization
    def __init__(self, angle, magnitude_unitless):
        self.angle = angle
        res = BOT_STEPS_360 / BOT_CIRCUMFERENCE

        #magnitude in steps
        self.magnitude = magnitude_unitless / res

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