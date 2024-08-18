import sys
n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
  tmp = list(map(int,sys.stdin.readline().split()))
  graph.append(tmp)

k = int(sys.stdin.readline())
for i in range(k):
  cnt = 0
  a,b,c,d = map(int,sys.stdin.readline().split())
  for j in range(a,c+1):
    for k in range(b,d+1):
      cnt += graph[j-1][k-1]
  print(cnt)