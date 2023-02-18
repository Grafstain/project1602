#В случайном порядке выводятся элементы списка без повторов.
import random
WORD_LIST = ["Один",
             "Два",
             "Три"]
new_list = WORD_LIST[:]
for i in range(len(new_list)):

    choise = random.choice(new_list)
    print(choise)
    new_list.remove(choise)


