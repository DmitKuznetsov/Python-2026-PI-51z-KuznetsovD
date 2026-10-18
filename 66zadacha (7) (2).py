m = int(input())
present_everywhere = None
for i in range(m):
    k = int(input())
    lesson = set()
    for j in range(k):
        lesson.add(input())
    if present_everywhere is None:
        present_everywhere = lesson
    else:
        present_everywhere &= lesson

for name in sorted(present_everywhere):
    print(name)