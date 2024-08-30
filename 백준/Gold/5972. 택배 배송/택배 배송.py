import sys
import heapq

INF = int(1e9)
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
cow = [INF for _ in range(n+1)]

def di(start):
  q = []
  heapq.heappush(q,(start,0))
  cow[1] = 0
  while q:
    now, cost = heapq.heappop(q)
    if cow[now] < cost:
      continue
    for i in graph[now]:
      if cost + i[1] < cow[i[0]]:
        cow[i[0]] = cost + i[1]
        heapq.heappush(q,(i[0],cow[i[0]]))
for _ in range(m):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
di(1)
print(cow[n])