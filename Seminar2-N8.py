N = int(input())
A = list(map(int, input().split(' ')))
for a in A:
    c1 = 0
    c2 = 0
    for b in A:
        if b < a:
            c1 += 1
            continue
        if b > a:
            c2 += 1
            continue
    if c1 == c2:
        print(a)
        break