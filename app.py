from tkinter import Tk, Canvas
import math
import numpy as np

class App():

    coordinates = []
    app = None
    canvas = None

    def __init__(self, size, bg):
        
        #initialization
        self.coordinates = []
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
        self.coordinates.clear()

    #draw based on mouse motion
    def draw(self, event):
        global lasx, lasy
        self.canvas.create_line((lasx, lasy, event.x, event.y), 
                        fill='red', 
                        width=2)
        #print(lasx, lasy, event.x, event.y)
        self.getVector([lasx, lasy], [event.x, event.y])
        lasx, lasy = event.x, event.y
        #self.coordinates.append([event.x, event.y])


    def createShape(self, last, current):
        #grab offset movement
        lenx = current[0] - last[0]
        leny = current[1] - last[1]

        magnitude = math.sqrt(lenx**2 + leny**2)
        vector = 

class Shape():

    vector = None    

    def __init__(self, vector):
       self.vector = vector 
