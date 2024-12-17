import turtle
class FOOD_CREATOR_CLASS:
    def create_food(self,random_xcor, random_ycor):
        self.food = turtle.Turtle()
        self.food.setposition(random_xcor, random_ycor)
        self.food.penup()
        self.food.color('yellow')
        self.food.shape('circle')
        self.food.shapesize(0.25, 0.25)
        return self.food


