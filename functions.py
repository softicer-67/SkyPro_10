
class Question:

    def __init__(self, question, complexity, answer):
        self.question = question
        self.complexity = complexity
        self.correct_answer = answer
        self.asked_the_question = False
        self.user_response = None
        self.points = 0

    def get_points(self):
        return self.points + int(self.complexity) * 10

    def is_correct(self):
        if self.user_response == self.correct_answer:
            self.asked_the_question = True
            return True
        return False

    def build_question(self):
        return f'Вопрос: {self.question}\nСложность: {self.complexity}/5'

    def build_feedback(self):
        if self.is_correct():
            self.get_points()
            return f'Ответ верный, получено: {self.get_points()} баллов\n'
        return f'Ответ не верный, верный ответ - {self.correct_answer}\n'


