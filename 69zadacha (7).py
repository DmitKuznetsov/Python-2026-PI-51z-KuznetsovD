m = int(input())
all_dishes = set()
for i in range(m):
    all_dishes.add(input())

n = int(input())
cooked = set()
for i in range(n):
    for dish in input().split():
        cooked.add(dish)

never_cooked = all_dishes - cooked
for dish in sorted(never_cooked):
    print(dish)