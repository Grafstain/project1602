# Генерирует персонажа, дает распределить 30 очков.
streight = 0
health = 0
wise = 0
dex = 0
attrPoints = 3
choise = None
STATUS = {
    "Всего очков": attrPoints,
    "Сила": streight,
    "Здоровье": health,
    "Мудрость": wise,
    "Ловкость": dex
}

while True:
    # print(f"У вас есть {attrPoints} очков ")
    print("""Выберите доступное действие:
    0 - закончить редактирование
    1 - добавить очки
    2 - убрать очки
    """)

    choise = input()
    if choise == "0":
        break
    elif choise == "1":
        print("Вы перешли к добавлению очков к аттрибутам")
        while int(STATUS["Всего очков"]) > 0:
            for i in STATUS:
                print(i, ": ", STATUS[i])
            print()

            print("""Куда вы хотите добавить очко?
0 - закончить редактирование
1 - добавить к силе
2 - добавить к здоровью
3 - добавить к мудрости
4 - добавить к ловкости""")
            choise = input()

            if choise == "0":
                break
            elif choise == "1":
                print("Вы добавили очко к силе")
                STATUS["Сила"] += 1
                STATUS["Всего очков"] -= 1
            elif choise == "2":
                print("Вы добавили очко к здоровью")
                STATUS["Здоровье"] += 1
                STATUS["Всего очков"] -= 1
            elif choise == "3":
                print("Вы добавили очко к мудрости")
                STATUS["Мудрость"] += 1
                STATUS["Всего очков"] -= 1
            elif choise == "4":
                print("Вы добавили очко к силе")
                STATUS["Ловкость"] += 1
                STATUS["Всего очков"] -= 1

        if STATUS["Всего очков"] == "0":
            print("Вы распределили все очки")
    elif choise == "2":
        print("Вы перешли к вычитанию очков из аттрибутам")
        while int(STATUS["Всего очков"]) > 0:
            for i in STATUS:
                print(i, ": ", STATUS[i])
            print()

            print("""От куда вы хотите отнять очко?
            0 - закончить редактирование
            1 - отнять очко от силы
            2 - отнять очко от здоровья
            3 - отнять очко от мудрости
            4 - отнять очко от ловкости""")
            choise = input()

            if choise == "0":
                break
            elif choise == "1":
                if int(STATUS["Сила"]) > 0:
                    print("Вы отняли очко от силы")
                    STATUS["Сила"] -= 1
                    STATUS["Всего очков"] += 1
                else:
                    print("Недостаточко очков силы")
            elif choise == "2":
                if int(STATUS["Здоровье"]) > 0:
                    print("Вы отняли очко от силы")
                    STATUS["Здоровье"] -= 1
                    STATUS["Всего очков"] += 1

                else:
                    print("Недостаточко очков здоровья")
            elif choise == "3":
                if int(STATUS["Мудрость"]) > 0:
                    print("Вы добавили очко к мудрости")
                    STATUS["Мудрость"] -= 1
                    STATUS["Всего очков"] += 1
            elif choise == "4":
                if int(STATUS["Ловкость"]) > 0:
                    print("Вы добавили очко к силе")
                    STATUS["Ловкость"] -= 1
                    STATUS["Всего очков"] += 1



