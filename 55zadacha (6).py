line_num = 0
found_num = -1
while True:
    s = input()
    if s == "СТОП":
        break
    line_num += 1
    if ("кот" in s or "Кот" in s) and found_num == -1:
        found_num = line_num
print(found_num)