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
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for position in SEGMENTS_START_POSITIONS:
            self.add_segment(position=position)

    def move(self):
        for seg in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg - 1].xcor()
            new_y = self.segment_list[seg - 1].ycor()
            self.segment_list[seg].goto((new_x, new_y))
        self.head.forward(20)

    def reset(self):
        # Make segments go off-screen.
        for seg in self.segment_list:
            seg.hideturtle()
        self.__init__()

    def collision_with_body(self):
        for segment in self.segment_list[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def extend(self):
        position = self.segment_list[-1].position()
        self.add_segment(position=position)

    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.setposition(position)
        segment.shape(name="square")
        segment.color("white")
        self.segment_list.append(segment)

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
