from tkinter import Tk, Canvas
import math
import numpy as np
import time
class App():

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

        #initalize app 
        self.app.mainloop()

    #get position on left click
    def left_click(self, event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    #enter when 
    def left_unclick(self, event):
        shape = Shape(self.lineBuf)
        self.shapes.append(shape)


    #draw based on mouse motion
    def draw(self, event):
        global lasx, lasy
        self.canvas.create_line((lasx, lasy, event.x, event.y), 
                        fill='red', 
                        width=2)
        
        if(self.canvasClear):
            self.createLine([0, 0], [event.x, event.y])
            self.canvasClear = False
            print("Added Start!!!!!!!!!!!!!!!!!!!!!!1")
            print(self.lineBuf[0].angle, self.lineBuf[0].magnitude)
        
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

class Line():

    angle = None    
    magnitude = None

    #initilize 
    def __init__(self, angle, magnitude):
        self.angle = angle
        self.magnitude = magnitude

    def angle(self):
        return self.angle

    def magnitude(self):
        return self.magnitude

class Shape():
    ANGLE_THRESH = 1
    MAGNITUDE_THRESH = 1
    start = []
    vectors = []

    def __init__(self, lines):
       