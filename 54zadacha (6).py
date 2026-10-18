line_num = 0
count = 0
first_num = -1
while True:
    s = input()
    if s == "СТОП":
        break
    line_num += 1
    if "кот" in s or "Кот" in s:
        count += 1
        if first_num == -1:
            first_num = line_num
print(count)
print(first_num)