import math
N = int(input())
n = N
i = 2
num_list = []
while (i<=N):
    if N % i ==0:
        N /= i
        print(i)
    else:
        i += 1