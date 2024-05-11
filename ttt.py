import sys

n,k = map(int,sys.stdin.readline().split())
group = list(map(int,sys.stdin.readline().split()))

tmp = []
for i in range(n-1):
  dif = group[i+1] - group[i]
  tmp.append((i,dif))
print(tmp)
tmp = tmp.
print(tmp)
