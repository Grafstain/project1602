# Программа словарь с парой сын-отец, по введеному сыну говорит кто отец

dict = {
    "Роман": "Александр",
    "Александр": "Андрей",
    "Андрей": "Прокофий"
}
choice = None
while choice != '0':
    print("""
Введите имя чьего отца вы хотите узнать 
    """)
    choice = input("").title()
    if choice in dict.keys():
        print(f"Отца {choice} зовут {dict[choice]}")
    else:
        print("Я такого не знаю")
    input("\nДля выхода нажмите Enter")
