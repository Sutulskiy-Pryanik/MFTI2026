A = list(input().split(' '))
m = 0
for a in A:
    if A.count(a) > m:
        m = A.count(a)
        cur = a
print(cur)