from functions import *
import random
import json


def get_json():
    with open('text.json', 'r') as f:
        txt = json.load(f)
        return txt


def get_question(txt_quest):
    questions_text = []
    for quest in txt_quest:
        questions_text.append(Question(quest['q'], quest['d'], quest['a']))
    random.shuffle(questions_text)
    return questions_text


def main():
    all_txt = get_json()
    count = 0
    my_points = 0
    quest = get_question(all_txt)
    print("Игра начинается!")
    for i in quest:
        print(i.build_question())
        answer = input('Ответ: ')
        i.user_response = answer
        print(i.build_feedback())
        if i.asked_the_question is True:
            my_points += i.get_points()
        count += 1

    print(f"Вот и все!\nОтвечено на {sum(i.asked_the_question for i in quest)} вопроса из {len(quest)}\nНабранно {my_points} баллов")


if __name__ == '__main__':
    main()

