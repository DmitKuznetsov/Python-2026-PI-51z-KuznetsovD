while True:
    p1 = input()
    p2 = input()

    if len(p1) < 8:
        print("Слишком короткий!")
    elif "123" in p1:
        print("Содержит 123!")
    elif p1 != p2:
        print("Пароли не совпадают!")
    else:
        print("OK")
        break