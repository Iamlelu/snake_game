import random
import turtle



class SNAKE_CLASS:
        def __init__(self):
            self.score = 0
            self.timer = 0.1
            self.snakes_list = []
            self.snakes_pos = [(0, 0), (-8, 0), (-16, 0)]

            for snake_po in self.snakes_pos:
                self.snake = turtle.Turtle()
                tur_colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown",
                               "White", "Gray", "Cyan", "Magenta", "Lime", "Maroon", "Navy",
                              "Olive", "Teal", "Aqua", "Fuchsia", "Silver", "Gold", "Beige", "Coral"]

                self.snake.color(random.choice(tur_colors))
                self.snake.shape('square')
                self.snake.shapesize(0.5, 0.5)
                self.snake.penup()
                self.snakes_list.append(self.snake)
                self.snake.goto(snake_po)

#add new segment
        def add_new_segment(self):
            new_snake = turtle.Turtle()
            tur_colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown",
                "Black", "White", "Gray", "Cyan", "Magenta", "Lime", "Maroon", "Navy",
                "Olive", "Teal", "Aqua", "Fuchsia", "Silver", "Gold", "Beige", "Coral"]

            new_snake.color(random.choice(tur_colors))

            new_snake.shape('square')
            new_snake.shapesize(0.5, 0.5)
            new_snake.penup()
            new_pos = self.snakes_list[len(self.snakes_list)-1].pos()
            self.snakes_list.append(new_snake)
            new_snake.goto(new_pos)


        def snake_move(self):
            for snake_part in range(len(self.snakes_list) - 1, 0, -1):
                x_cor = self.snakes_list[snake_part - 1].xcor()
                y_cor = self.snakes_list[snake_part - 1].ycor()
                self.snakes_list[snake_part].goto(x_cor, y_cor)
            self.snakes_list[0].forward(8)

        def snake_up(self):
            if self.snakes_list[0].heading() == 270:
                pass
            else:
                self.snakes_list[0].setheading(90)
        def snake_down(self):
            if self.snakes_list[0].heading() == 90:
                pass
            else:
                self.snakes_list[0].setheading(270)
        def snake_left(self):
            if self.snakes_list[0].heading() == 0:
                pass
            else:
                self.snakes_list[0].setheading(180)
        def snake_right(self):
            if self.snakes_list[0].heading() == 180:
                pass
            else:
                self.snakes_list[0].setheading(0)
        def snake_screen_protocol(self,score_tur_var):
            if self.snakes_list[0].xcor() >= 350 or self.snakes_list[0].xcor() <= -350 or self.snakes_list[0].ycor() >= 350 or self.snakes_list[0].ycor() <= -350:
                from game_over_file import GAME_OVER_CLASS
                game_over_tur = GAME_OVER_CLASS()
                game_over_tur.game_over_func()
                score_tur_var.score_saver(self.score)

                return True

        def snake_self_suicide(self,score_tur):
            for k in range(len(self.snakes_list) - 1):
                m = k + 1
                if self.snakes_list[0].distance(self.snakes_list[m]) <= 0:
                    from game_over_file import GAME_OVER_CLASS
                    game_over_tur = GAME_OVER_CLASS()
                    game_over_tur.game_over_func_self()
                    score_tur.score_saver(self.score)
                    value = True
                    return value
        def detect_food(self,food_tur,food_tur_var,score_tur_var):
            if self.snakes_list[0].distance(food_tur) <= 8:
                food_tur.hideturtle()
                random_xcor = random.randint(-340, 340)
                random_ycor = random.randint(-300, 340)
                food_tur_var.create_food(random_xcor, random_ycor)
                self.score += 1
                self.add_new_segment()
                score_tur_var.score_writer_func(self.score)
                self.timer -= 0.005






