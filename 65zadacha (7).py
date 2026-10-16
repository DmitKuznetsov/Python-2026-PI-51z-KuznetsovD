m = int(input())
library = set()
for i in range(m):
    library.add(input())

n = int(input())
for i in range(n):
    book = input()
    if book in library:
        print("YES")
    else:
        print("NO")