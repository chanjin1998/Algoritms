import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
cnt = 0
num.sort()

n , m  = 0, N - 1
while (n<m):
    if num[n] + num[m] == M:
        n += 1
        m -= 1
        cnt += 1
    elif num[n] + num[m] < M:
        n += 1
    else:
        m -= 1
print(cnt)