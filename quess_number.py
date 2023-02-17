#  computer quess choosen human's number
# ©Grafstain


count = 0
left_zone = 0
right_zone = 100
number = (right_zone-left_zone)//2
print("Загадайте число от 0 до 100, а я попробую его угадать. "
      "Отвечать нужно 'да' или 'нет',если нет нужно будет уточнить 'меньше' или 'больше'")
while True:

    print(f"Ваше число {number}?")
    answer = input()
    if answer.lower() == "да":
        count += 1
        break
    else:
        print("Ваше число больше или меньше?")
        answer = input()
        if answer.lower() == "больше":
            left_zone = number
            count += 1
            number = number + (right_zone - left_zone) // 2
            print(f"Ваше число в диапазоне {left_zone}-{right_zone}")
        elif answer.lower() == "меньше":
            right_zone = number
            count += 1
            number = number - (right_zone - left_zone) // 2
            print(f"Ваше число в диапазоне {left_zone}-{right_zone}")
print(f"У меня получилось угадать ваше число за {count} попыток")
