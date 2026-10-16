m = int(input())
fridge = set()
for i in range(m):
    fridge.add(input())

n = int(input())
for i in range(n):
    parts = input().split()
    recipe_name = parts[0]
    ingredients = set(parts[1:])
    if ingredients <= fridge:
        print(recipe_name)