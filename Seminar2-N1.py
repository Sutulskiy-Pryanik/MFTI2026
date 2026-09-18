s = input('карты: ')
A = list(map(int, s.split(' ')))
n = int(A[0])
A[0] = 0
res = (n*(n + 1))//2
for i in A:
    res -= i
print(res)
