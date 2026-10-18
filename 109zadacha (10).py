n = int(input())
pairs = []
for i in range(n):
    pos, letter = input().split()
    pairs.append((int(pos), letter))

pairs.sort()
word = ""
for pos, letter in pairs:
    word += letter
print(word)