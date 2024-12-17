import turtle
class GAME_OVER_CLASS:
    def game_over_func(self):
        game_over = turtle.Turtle()
        game_over.goto(-30, 0)
        game_over.color('white')
        game_over.hideturtle()
        game_over.write(f"YOUR SNAKE DIED\n  GAME OVER")

    def game_over_func_self(self):
        game_over = turtle.Turtle()
        game_over.goto(-30, 0)
        game_over.color('white')
        game_over.hideturtle()
        game_over.write(f'SELF SUICIDE \nSTAY SHARP')

