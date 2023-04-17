from turtle import Turtle
ALIGNMENT='center'
FONT=('Arial', 16, 'normal')

class Game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.write('GAME OVER',align=ALIGNMENT, font=FONT)