from turtle import Turtle
starting_position=[(0,0),(-20,0),(-40,0)]
move_distance=20
Up =90
Down = 270
Left= 180
Right = 0



class Snake():
    
    def __init__(self):
      self.segments = []
      self.create_snake()
      self.head =self.segments[0]
      
      
    def create_snake(self):
       for position in starting_position:
           self.add_segment(position)
           # yaha se nkl ke add_segment shift kiya to extend the snak tail jab score krta rehenga
            # new_segment=Turtle("square")
            # new_segment.color("white")
            # new_segment.penup()
            # new_segment.goto(position)
            # self.segments.append(new_segment)
            
    def add_segment(self,position):
           new_segment=Turtle("square")
           new_segment.color("lightgreen")
           

           new_segment.penup()
           new_segment.goto(position)
           self.segments.append(new_segment)
               
            #add new segment to the snake
            
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)   # move off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.setheading(0)   

    def extend(self): 
      self.add_segment(self.segments[-1].position())       
        
    
    def move(self):
        for  seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y= self.segments[seg_num -1].ycor()
            self.segments[seg_num ].goto(new_x , new_y)
        
        self.head.forward(move_distance)
    
    
    def Up(self):
        if self.head.heading()!=Down:
         self.head.setheading(Up)

    def Down(self):
       if self.head.heading()!=Up: 
        self.head.setheading(Down)

    def Left(self):
       if self.head.heading()!=Right: 
        self.head.setheading(Left)

    def Right(self):
       if self.head.heading()!=Left: 
        self.head.setheading(Right)
    
    
    def hide(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  
