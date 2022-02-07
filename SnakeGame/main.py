from time import time
from turtle import Screen,Turtle
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]

segments_list = []

#Creating 3 turtles
for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments_list.append(segment)

game_is_on = True

#Will Run till the game is lost
while game_is_on:
    screen.update() #Will refresh the screen
    time.sleep(0.1) #Will sleep for 0.1 seconds
    
    #This code makes the body follow the head
    for seg_num in range(len(segments_list)-1,0,-1):
        new_x = segments_list[seg_num-1].xcor()
        new_y = segments_list[seg_num-1].ycor()
        segments_list[seg_num].goto(new_x,new_y)
    
    segments_list[0].forward(20)
    segments_list[0].left(90)




screen.exitonclick()

