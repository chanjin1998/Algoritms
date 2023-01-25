import sys
N, M = map(int,sys.stdin.readline().split(" "))
arr = list(map(int, input().split(" ")))
result = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        result[i] = arr[i]
    else:
        result[i] = result[i - 1] + arr[i]

for _ in range(M):
    i, j = map(int,sys.stdin.readline().split(" "))
    if i == 1:
        print(result[j - 1])
    else:
        print(result[j - 1] - result[i - 2])