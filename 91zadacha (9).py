s = input()
allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
for c in s:
    if c not in allowed:
        print("Неверный символ:", c)
        break
else:
    print("OK")