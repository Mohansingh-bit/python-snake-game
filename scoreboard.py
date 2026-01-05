from turtle import Turtle
ALIGNMENT="center"
FONT =("Arial" , 24, "normal")
HIGH_SCORE_FILE = "high_score.txt"



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score = 0  
         
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        #self.write(f"Score:{self.score}", align = ALIGNMENT ,font = FONT)
        
        try:
             with open("high_score.txt", "r") as file:
              content = file.read()
             if content.strip():          # check if not empty
              self.high_score = int(content)
             else:
               self.high_score = 0

        except FileNotFoundError:
             self.high_score = 0
        
        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.color("green")
        self.score_turtle.goto(-80, 265)

    
        self.high_score_turtle = Turtle()
        self.high_score_turtle.hideturtle()
        self.high_score_turtle.penup()
        self.high_score_turtle.color("red")
        self.high_score_turtle.goto(110, 265)
        
        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.penup()
        self.game_over_turtle.color("white")

     
             
        self.line = Turtle()
        self.line.hideturtle()
        self.line.penup()
        self.line.color("red")
        self.bg_bar = Turtle()
        self.bg_bar.hideturtle()
        self.bg_bar.penup()
        self.bg_bar.color("white")   
        self.draw_score_bar()
   
        self.update_score()
    
        
        
    def update_score(self):
        self.score_turtle.clear()
        self.high_score_turtle.clear()

        self.score_turtle.write(
        f"Score: {self.score}",
        align="center",font=("Courier", 20, "bold") )

        self.high_score_turtle.write(
        f"High Score: {self.high_score}",
        align="center",font=("Courier", 20, "bold"))
    
     

 
    def increase_score(self):
        self.score += 1
        self.update_score() 
        
    def reset(self):
        self.clear()
        self.game_over_turtle.clear()   

        self.line.clear()       
        self.line.hideturtle()   
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write(str(self.high_score))
              
        self.score = 0
        self.goto(0,270)
        self.draw_score_bar()   
        self.update_score()
    
    def draw_score_bar(self):
        self.bg_bar.clear()
        self.bg_bar.goto(-300, 300)
        self.bg_bar.begin_fill()
        self.bg_bar.pendown()

        self.bg_bar.forward(600)
        self.bg_bar.right(90)
        self.bg_bar.forward(40)
        self.bg_bar.right(90)
        self.bg_bar.forward(600)
        self.bg_bar.right(90)
        self.bg_bar.forward(40)
        self.bg_bar.right(90)

        self.bg_bar.end_fill()
        self.bg_bar.penup()
   
    def game_over(self , snake=None,food=None):
          if snake:
            snake.hide()
          if food:
            food.hide()

    
          self.line.clear()   
          self.line.goto(-100, 50)
          self.line.pendown()
          self.line.showturtle()
          self.line.forward(200)
          self.line.penup()
          self.game_over_turtle.clear()
          self.game_over_turtle.goto(0, 70)
          self.game_over_turtle.write(
        "GAME OVER",
        align="center",  font=("Arial", 24, "normal"))