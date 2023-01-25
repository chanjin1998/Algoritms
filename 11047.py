import sys
N,K = map(int,sys.stdin.readline().split())
coin = []
cnt = 0
for i in range(N):
    coin.append(int(sys.stdin.readline().strip()))
for j in range(N-1,-1,-1):
    if K // coin[j] >0:
        cnt += K // coin[j]
        K = K % coin[j]
    if K == 0:
        break
print(cnt)