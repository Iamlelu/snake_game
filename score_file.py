import turtle


class SCORE_CLASS():

    def  __init__(self):
        self.score_tur = turtle.Turtle()
        self.score_tur.goto(-30, 330)
        self.score_tur.color('white')
        self.score_tur.hideturtle()

    def score_writer_func(self,score):
        self.score_tur.clear()
        self.score_tur.write(f'FOODS ATE - {score}')

    def score_saver(self,score):
        with open('high_score_data', mode='a') as score_data_file:
            score_data_file.write(f'\n{int(score)}')