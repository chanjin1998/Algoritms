N = int(input())
a = 1
for i in range(N):
    if N >=1 and N !=0:
        a = a * N
        N -= 1
    elif N == 0:
        a = 1
        break
print(a)