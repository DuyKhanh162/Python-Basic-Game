from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f'Level: {self.score}', False, 'left', FONT)

    def plus_one(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', FONT)
