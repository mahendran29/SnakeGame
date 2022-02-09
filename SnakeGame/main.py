import time
from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scorecard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

#Will Run till the game is lost
while game_is_on:

    screen.update()         #Will refresh the screen
    time.sleep(0.1)         #Will sleep for 0.1 seconds
    snake.move()

    #Detect Collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scorecard.increase_score()
    
    #Detect Collision with Wall
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        scorecard.reset()
        snake.reset()
    
    #Detect Collision with Tail
    for segment in snake.segments_list[1:]:
        if snake.head.distance(segment)<10:
            scorecard.reset()
            snake.reset()
    
   
screen.exitonclick()
