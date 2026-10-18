n = int(input())
names = [input() for _ in range(n)]

seen = set()
duplicates = set()
for name in names:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

count = 0
for name in names:
    if name in duplicates:
        count += 1
print(count)