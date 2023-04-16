from turtle import Turtle
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):

        for i in range(3):
            new_segment = Turtle()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setx(-i * MOVE_DISTANCE)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
