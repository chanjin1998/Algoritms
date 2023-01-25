import sys
n,k = map(int,sys.stdin.readline().split())
res=[]
alpha = list(map(int,sys.stdin.readline().split()))
res = [0 for _ in range(n-k+1)]
for i in range(n-k+1):
    sum = 0
    for j in range(i,i+k):
        sum += alpha[j]
    res[i] = sum
print(max(res))
