#  count true and false for throwing a coin 100 times
# ©Grafstain

import random

i, count_true, count_false = 0, 0, 0
while i < 100:

    throw = random.randint(0, 1)
    if throw:
        count_true += 1
        print("Выпал Орел")
    else:
        count_false += 1
        print("Выпала Решка")
    i += 1
print("Всего выпало орлов: ", count_true, "\nВсего выпало решек: ", count_false)
