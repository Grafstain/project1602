# Игра угадай анаграмму
# Компьютер выбирает слово и хаотически переставляет его буквы
# Задача игрока отгадать слово
import random

WORDS = ('питон', "макака", "рома", "слива", "туман")

word = random.choice(WORDS)
correct = word
anagramm = ""
while word:
    position = random.randrange(len(word))
    letter = word[position]
    anagramm += letter
    word = word[:position] + word[(position + 1):]

# Начало игры
print("""
        Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так чтобы получилось осмысленное слово.
    (Для выхода нажминет Enter без ввода вашего варианта.)
    """)
print("Вот анаграмма : ", anagramm)
quess = input("\nПопробуйте отгадать слово: ")
while quess != correct and quess != "":
    print("К сожалению, не верно.")
    quess = input("Попробуйте отгадать исходное слово: ")
if quess == correct:
    print("Ура, вы отгадали! Спасибо за игру.")
input("\n Для выхода нажмите Enter ")
