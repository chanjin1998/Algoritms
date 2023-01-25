import sys
n,k = map(int,sys.stdin.readline().split())
circle = [i for i in range(1,n+1)]
res = []
while (1):
    if len(circle) == 0:
        break
    res.append(circle[(k-1)%len(circle)])
    del circle[(k-1)%len(circle)]
    k += 3
print(res)
