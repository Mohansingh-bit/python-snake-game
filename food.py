from turtle import Turtle
import random

class Food(Turtle):
    
    
    def __init__(self,left,right,bottom,top,snake_segments=None):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 ,stretch_wid =0.5)
        self.color("red")
        self.speed("fast")
        
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

        self.refresh(snake_segments)
        
    def refresh(self,snake_segments=None):   
        x = random.randint(self.left + 20, self.right - 20)
        y = random.randint(self.bottom + 20, self.top - 20)
        
        if snake_segments:
         while any(seg.distance(x, y) < 15 for seg in snake_segments):
            x = random.randint(self.left + 20, self.right - 20)
            y = random.randint(self.bottom + 20, self.top - 20)

        self.goto(x ,y)
    
    def reset(self):
        self.refresh()        
        
        
    def hide(self):
        self.goto(1000, 1000)  