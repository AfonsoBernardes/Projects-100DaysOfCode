from turtle import Turtle

SEGMENTS_START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        # Snake starts as 3 white squares.
        self.segment_list = []
        for position in SEGMENTS_START_POSITIONS:
            segment = Turtle()
            segment.penup()
            segment.setposition(position)
            segment.shape(name="square")
            segment.color("white")
            self.segment_list.append(segment)

        self.head = self.segment_list[0]

    def get_segment_list(self):
        return self.segment_list

    def move(self):
        segment_list = self.get_segment_list()
        for seg in range(len(segment_list) - 1, 0, -1):
            new_x = segment_list[seg - 1].xcor()
            new_y = segment_list[seg - 1].ycor()
            segment_list[seg].goto((new_x, new_y))
        self.head.forward(20)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
