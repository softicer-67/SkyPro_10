import random
import secrets


class Question:

    def __init__(self, question, complexity, correct_answer):
        self.question = question
        self.complexity = complexity
        self.correct_answer = correct_answer
        self.asked_the_question = False
        self.user_response = None
        self.points = 0

    def get_points(self):
        return self.points + int(self.complexity) * 10

    def is_correct(self, user_response, correct_answer):
        self.user_response = user_response
        if user_response == correct_answer:
            self.correct_answer = correct_answer
            return self.build_positive_feedback(self.points)
        else:
            return self.build_negative_feedback(self.correct_answer)

    def build_question(self, question, complexity):
        self.question = question
        self.complexity = complexity
        print(f'Вопрос: {question}\nСложность: {complexity}/5')

    def build_positive_feedback(self, points):
        self.points = points
        print(f'Ответ верный, получено: {self.get_points()} баллов\n')

    def build_negative_feedback(self, correct_answer):
        self.correct_answer = correct_answer
        print(f'Ответ не верный, верный ответ - {correct_answer}\n')


def get_question():
    quest1 = "How many days do we have in a week?", 5, 7
    quest2 = "How many letters are there in the English alphabet?", 3, 26
    quest3 = "How many sides are there in a triangle?", 2, 3
    quest4 = "How many years are there in one Millennium?", 2, 1000
    quest5 = "How many sides does hexagon have?", 4, 6
    quest = secrets.choice([quest1, quest2, quest3, quest4, quest5])
    return quest


def main():
    count = 0
    good_answer = 0
    my_points = 0
    print("Игра начинается!")
    while count != 5:

        quest = get_question()
        p = Question(quest[0], quest[1], quest[2])
        p.build_question(quest[0], quest[1])
        user_response = input('Ответ: ')
        print('До', p.get_points())
        if user_response == str(quest[2]):
            p.is_correct(user_response, str(quest[2]))
            good_answer += 1
            my_points += int(p.get_points())
        else:
            p.build_negative_feedback(quest[2])
        count += 1

    print(f"Вот и все!\nОтвечено на {good_answer} вопроса из {count}\nНабранно {my_points} баллов")


if __name__ == '__main__':
    main()

