A = list(input().split(' '))
print(*[A[min(i - 2*(i%2) + 1, len(A) - 1)] for i in range(0,len(A))])