a, b = input().split()

if a == "да" and b == "да":
    print("Ты уверен в себе — вперёд!")
elif a == "да" and b == "нет":
    print("Подумай ещё раз.")
elif a == "нет" and b == "да":
    print("Попробуй что-то новое.")
else:
    print("Оставайся дома.")