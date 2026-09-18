n, s = input('кол-во групп и строка:').split(' ')
n = int(n)
N = len(s)
A = [s[i*(N//n):(i+1)*(N//n)] for i in range(0,n)]
s1 = ''
for i in range(0,n):
    s1 += A[i][::-1]
print(s1)
