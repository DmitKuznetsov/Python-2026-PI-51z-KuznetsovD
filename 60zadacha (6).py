total = 0
count = 0
stopped = False
while True:
    x = int(input())
    if x == 0:
        break
    count += 1
    total += x
    if total > 100:
        stopped = True
        break
if stopped:
    print("СТОП")
    print(count)
else:
    print("ОК")