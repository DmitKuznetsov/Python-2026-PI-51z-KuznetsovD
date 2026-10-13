n = int(input())
found = False
for i in range(n):
    s = input()
    if "кот" in s or "Кот" in s:
        found = True
        break
print("МЯУ" if found else "НЕТ")