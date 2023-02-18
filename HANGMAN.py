# Игра виселица(HANGMAN)
# В которой вы пытаетесь отгадать загаданное компьютером слово
# При неправильном ответе состояние человека на висилице меняется,через 8 ошибок он умрет и вы проиграете.

import random

HANGMAN = ("""
_____________
|
|
|
|
|
""",
"""
_____________
|       |
|
|
|
|
       """,
"""
_____________
|       |
|       0
|
|
|
       """,
"""
_____________
|       |
|       0
|       |
|       
|      
       """,
"""
_____________
|       |
|       0
|      /|\\
|       
|      
       """,
"""
_____________
|       |
|       0
|      /|\\
|       |
|      
       """,
"""
_____________
|       |
|       0
|      /|\\
|       |
|      / \\
       """)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("эльвира", "рома", "стол", "стул", "волейбол")

word = random.choice(WORDS)
# состояние отгаданного игроком слова
so_far = '-' * len(word)
wrong = 0
# список букв названных игроком
used = []

print("Добро пожаловать в игру Виселица. Удачи вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже предлагали следующие буквы\n", used)
    print("\nОтгаданное вами слово сейчас выглядит так\n", so_far)
    quess = input("Введите букву: ")
    quess = quess.lower()
    while quess in used:
        print("Вы уже предлагали букву ", quess)
        quess = input("\n\nВведите букву: ")
        quess = quess.lower()
    used.append(quess)

    if quess in word:
        print("Да буква ", quess, "есть в слове!")
        new = ""
        for i in range(len(word)):
            if quess == word[i]:
                new += quess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("К сожалению буквы ", quess, "нет в слове")
        print("Загаданное слово", word)
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили!")
else:
    print("\nВы отгадали!")
    print("\nБыло загадано слово: ", word)
input("\n\nНажмите Enter для выхода")
