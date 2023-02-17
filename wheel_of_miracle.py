import random

QUESTIONS = ("Столица Великобритании",
             "Столица России",
             "Как называется столовы прибор, предназначенный для пасты")
CORRECT_ANSWERS = (
    "лондон",
    "москва",
    "вилка"
)
score = 0
last_questions = QUESTIONS
last_answers = CORRECT_ANSWERS
print("""       Игра Поле чудес
    Вам будет задан вопрос вы должны правильно ответить за 3 попытки.
        """)
while input(" Для продолжения нажмите Enter\n") != '':
    pass
while True:
    if last_questions:
        pass
    else:
        print(f"Вы ответили на все вопросы и всего зарботали {score}очков.")
        break
    position = random.randrange(len(last_questions))
    question = last_questions[position]
    print("Ваш вопрос: ", last_questions[position])
    for i in range(3):
        answer = input("Ваш ответ: ").lower()
        if answer == last_answers[position]:
            score += 100
            print(f"Вы выиграли, и заработали 100 очков, всего у вас {score} очков")
            break
        else:
            print(f"Вы ответили не верно, у вас осталось {2 - i} попыток")
            if input("Вам нужна подсказка? ").lower() == 'да':
                print(f"Ответ на этот вопрос состоит из {len(last_answers[position])} букв")
    if input("Хотите сыграть еще раз? ") == 'да':
        last_questions = last_questions[:position] + last_questions[position+1:]
        last_answers = last_answers[:position] + last_answers[position+1:]

        continue
    else:
        break
