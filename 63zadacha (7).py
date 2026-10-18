m = int(input())
english = set()
for i in range(m):
    english.add(input())

n = int(input())
german = set()
for i in range(n):
    german.add(input())

only_one = (english - german) | (german - english)
if only_one:
    print(len(only_one))
else:
    print("NO")