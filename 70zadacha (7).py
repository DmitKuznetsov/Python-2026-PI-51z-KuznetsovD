first = set(map(int, input().split()))
second = set(map(int, input().split()))

symm_diff = first ^ second
if symm_diff:
    print(" ".join(str(x) for x in sorted(symm_diff)))
else:
    print("EMPTY")