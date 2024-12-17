""" this is snake game showcasing classes and objects, file handling, gui using turtle graphics"""


import turtle
import time
import random


from score_file import SCORE_CLASS
from high_score_file import HIGH_SCORE_CLASS
from snake_file import SNAKE_CLASS
from food_creator_file import FOOD_CREATOR_CLASS




#screen features
screen = turtle.Screen()
screen.title('SIMPLE SNAKE GAME')
screen.setup(700,700)
screen.bgcolor('black')
screen.tracer(0)



#players score writer
score_tur_var = SCORE_CLASS()


# high score writer and stripping the spaces and converting to int
high_score_var = HIGH_SCORE_CLASS()# creating the high score turtle
high_score_var.high_score_writer_func()# call the function to write


# creating the object for the snake to appear on snake
snake_var = SNAKE_CLASS()






# call food
random_xcor = random.randint(-240, 240)
random_ycor = random.randint(-240, 240)

#create food on screen randomly
food_tur_var = FOOD_CREATOR_CLASS()
food_tur_var.create_food(random_xcor, random_ycor)
game = True



while game:

    screen.listen()
    screen.update()
    time.sleep(snake_var.timer)
    snake_var.snake_move()
    screen.onkey(key='Left', fun=snake_var.snake_left)
    screen.onkey(key='Right', fun=snake_var.snake_right)
    screen.onkey(key='Up', fun=snake_var.snake_up)
    screen.onkey(key='Down', fun=snake_var.snake_down)

    #food detection
    snake_var.detect_food(food_tur_var.food,food_tur_var,score_tur_var)


    #checking screen protocols
    confirmation_screen_protocol = snake_var.snake_screen_protocol(score_tur_var)

    if confirmation_screen_protocol:
        break

    #checking for self suicide
    confirmation_suicide_protocol = snake_var.snake_self_suicide(score_tur_var)
    if confirmation_suicide_protocol:
        game = False
        break


screen.mainloop()