import sys

n,k = map(int,sys.stdin.readline().split())
group = list(map(int,sys.stdin.readline().split()))

tmp = []
val = []
for i in range(n-1):
  dif = group[i+1] - group[i]
  tmp.append(dif)
tmp.sort(reverse=True)

print(sum((tmp[k-1:])))