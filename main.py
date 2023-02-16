#  child with question why?
# ©Grafstain

answer = ""
print("Привет сынок")
print("Мам у меня есть вопрос, почему небо синее?")
while True:
    answer = input()
    if answer.lower() == "потому что":
        print("А, понятно")
        break
    else:
        print("Почему " + answer.lower() + "?")

