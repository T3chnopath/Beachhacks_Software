from tkinter import Tk, Canvas, Button
import math
import numpy as np
import time

from bluetooth import *
class App():
    bluetooth = Bluetooth()
    canvasClear = True
    lineBuf = []
    shapeBuf = None 
    shapes = []
    app = None
    canvas = None

    def __init__(self, size, bg):
        
        #initialization
        self.app = Tk()
        self.app.geometry(size)
        
        self.canvas = Canvas(self.app, bg=bg)
        self.canvas.pack(anchor="nw", fill="both", expand=1)

        #bind left click and mouse motion 
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<ButtonRelease-1>", self.left_unclick)
        self.canvas.bind("<B1-Motion>", self.draw)
    
        btn = Button(self.app, text='Draw', width=10,
             height=5, bd='10', command=self.send)
 
        btn.place(x=0, y=100)
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
        
        if(self.canvasClear):
            self.createLine([0, 0], [event.x, event.y])
            self.canvasClear = False
        
        else:
            self.createLine([lasx, lasy], [event.x, event.y])   

        lasx, lasy = event.x, event.y
        time.sleep(0.01)

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
        self.bluetooth.send(self.shapes)

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
    start = []
    _vectors = []

    #initalization
    def __init__(self, lines):
        for x in lines:
            self._vectors.append(x)

    def getVectors(self):
        return self._vectors