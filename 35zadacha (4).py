p1 = input()
p2 = input()

if len(p1) < 8:
    print("Слишком короткий!")
elif p1 != p2:
    print("Пароли не совпадают!")
else:
    print("OK")