total = 0
count = 0
answer = -1
while True:
    x = int(input())
    if x == 0:
        break
    count += 1
    total += x
    if total == 10 and answer == -1:
        answer = count
print(answer)