from tkinter import Tk, Canvas
import numpy as np

class App():

    coordinates = []
    app = None
    canvas = None

    def __init__(self, size, bg):
        
        #initialization
        self.app = Tk()
        self.app.geometry(size)
        
        self.canvas = Canvas(self.app, bg=bg)
        self.canvas.pack(anchor="nw", fill="both", expand=1)

        #bind left click and mouse motion 
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.draw)

        #initalize app 
        self.app.mainloop()

    #get position on left click
    def click(self, event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    #draw based on mouse motion
    def draw(self, event):
        global lasx, lasy
        self.canvas.create_line((lasx, lasy, event.x, event.y), 
                        fill='red', 
                        width=2)
        lasx, lasy = event.x, event.y

        

class Shape():

    vector = None    

    def __init__(self, vector):
       self.vector = vector 
