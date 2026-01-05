from turtle import Turtle ,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard   
from restart_button import RestartButton
import winsound
import threading

LEFT_WALL = -280
RIGHT_WALL = 280
BOTTOM_WALL = -300
TOP_WALL = 255   
def show_start_screen(screen):
    start_turtle = Turtle()
    start_turtle.hideturtle()
    start_turtle.penup()
    start_turtle.color("white")
    
    
    start_turtle.goto(0, 50)
    start_turtle.write("🐍 SNAKE GAME 🐍", align="center", font=("Arial", 30, "bold"))
    
    
    instructions = [
        "Use arrow keys to move the snake",
        "Eat the food to score points",
        "Avoid walls and your tail"
    ]
    y_pos = 0
    for line in instructions:
        start_turtle.goto(0, y_pos)
        start_turtle.write(line, align="center", font=("Arial", 18, "normal"))
        y_pos -= 30  

    start_turtle.goto(0, -100)
    start_turtle.write("Press SPACE to start", align="center", font=("Arial", 20, "bold"))
    
    return start_turtle


screen=Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")

start_turtle = show_start_screen(screen)
screen.update()

game_started = False

def start_game():
    global game_started
    game_started = True
    start_turtle.clear()  

screen.listen()
screen.onkey(start_game, "space")

while not game_started:
  screen.update()

snake=Snake()
food = Food(LEFT_WALL, RIGHT_WALL, BOTTOM_WALL, TOP_WALL,snake.segments)


scoreboard=Scoreboard()

def restart_game():
    global game_is_on
    scoreboard.clear()
    scoreboard.reset()
    snake.reset()
    food.reset()  
    restart_button.hide()  
    screen.update()      
    game_is_on = True
    
    


screen.listen()

screen.onkey(snake.Up ,"Up")
screen.onkey(snake.Down ,"Down")
screen.onkey(snake.Left ,"Left")
screen.onkey(snake.Right ,"Right")
screen.onkey(restart_game, "r")
screen.onkey(restart_game, "R")
restart_button = RestartButton(restart_game)

def play_eat_sound():
    
    #threading.Thread(target=lambda: winsound.Beep(800, 100)).start()
    winsound.PlaySound("eat.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


# starting_position=[(0,0),(-20,0),(-40,0)]
# segments=[]

# for position in starting_position:
#     new_segment=Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)


# # segment_2=Turtle("square")
# # segment_2.color("white")
# # segment_2.goto(-20 , 0)


# # segment_3=Turtle("square")
# # segment_3.color("white")
# # segment_3.goto(-40 ,0)
def play_collision_sound():
    winsound.Beep(500, 200)  
game_is_on = True
while True:
    screen.update()

    if game_is_on:
        time.sleep(0.1)
        snake.move()

        
        if snake.head.distance(food) < 15:
            food.refresh(snake.segments)
            snake.extend()
            scoreboard.increase_score()
            play_eat_sound()   
        
        if (
            snake.head.xcor() > 285 or snake.head.xcor() < -285 or
            snake.head.ycor() > TOP_WALL or snake.head.ycor() < -285
        ):
            scoreboard.game_over(snake=snake, food=food)  
            restart_button.show()
            play_collision_sound()   
            game_is_on = False
        
  
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
             scoreboard.game_over(snake=snake, food=food)   
             restart_button.show()
             play_collision_sound()   
             game_is_on = False
             break
        
        
        
        
#for  seg_num in range(len(segments)-1,0,-1):
#         new_x = segments[seg_num -1].xcor()
#         new_y= segments[seg_num -1].ycor()
#         segments[seg_num ].goto(new_x , new_y)
    
#     segments[0].forward(20)

screen.exitonclick()