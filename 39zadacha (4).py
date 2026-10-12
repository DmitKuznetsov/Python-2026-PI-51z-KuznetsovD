n = int(input())
total = 0
for digit in str(abs(n)):
    total += int(digit)
print(total)