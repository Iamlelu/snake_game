import turtle
class HIGH_SCORE_CLASS:
    def __init__(self):
        self.high_score_tur = turtle.Turtle()
        self.high_score_tur.goto(-300, 310)
        self.high_score_tur.color('white')
        self.high_score_tur.hideturtle()
        self.default_record_value = 0
        self.int_scores = []

    def high_score_writer_func(self):
        with open('high_score_data', mode='r') as high_score_file:
            all_scores = high_score_file.readlines()

            #converting the string and stripped scores into integer scores
            for unstripped_string_scores in all_scores:
                self.int_scores.append(int(unstripped_string_scores.strip()))
                max_score = max(self.int_scores)
        self.high_score_tur.clear()
        self.high_score_tur.write(f' RECORD- {max_score}')
