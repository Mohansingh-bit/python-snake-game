from turtle import Turtle

class RestartButton(Turtle):

    def __init__(self, restart_callback):
        super().__init__()
        self.restart_callback = restart_callback
        self.hideturtle()
        self.penup()
        self.color("white")

    def show(self):
        self.goto(0, -40)
        self.write("RESTART", align="center", font=("Courier", 20, "bold"))
        self.goto(0, -70)
        self.write("(Click Here)", align="center", font=("Courier", 12, "normal"))
        self.showturtle()
        self.onclick(self.on_click)

    def hide(self):
        self.clear()
        self.onclick(None)
        self.hideturtle()

    def on_click(self, x, y):
        self.hide()
        self.restart_callback()
