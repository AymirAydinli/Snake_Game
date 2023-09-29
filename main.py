from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
snake.move()
print(snake.head)
for seg in snake.segments:
    print(snake.head.distance(seg))
    print(seg.position())
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



    

    # Detect collsion with food
    if snake.head.distance(food) < 15:
        snake.extend()
        score.score_increase()
        food.refresh()


    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.ycor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()





    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
