
from turtle import Turtle

starting_positions = [(0,0),(-20,0),(-40,0)]
move_forward = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    segments_list = []

    def __init__(self):
        self.segments_list= []
        self.create_snake()
        self.head = self.segments_list[0]
    
    def create_snake(self):
        for position in starting_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments_list.append(segment)
    
    def move(self):
         for seg_num in range(len(self.segments_list)-1,0,-1):
             new_x = self.segments_list[seg_num-1].xcor()
             new_y = self.segments_list[seg_num-1].ycor()
             self.segments_list[seg_num].goto(new_x,new_y)
         self.head.forward(20)
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
        
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)