
from turtle import Turtle

starting_positions = [(0,0),(-20,0),(-40,0)]
move_forward = 20

class Snake:
    segments_list = []

    def __init__(self):
        self.segments_list= []
        self.create_snake()
    
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
         self.segments_list[0].forward(20)
         self.segments_list[0].left(90)