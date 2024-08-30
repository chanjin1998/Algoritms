import sys
import heapq

INF = int(1e4)
n,d = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(INF+1)]
distance = [INF for _ in range(INF+1)]

def di():
  q = []
  heapq.heappush(q,(0,0))
  while q:
    now, cost = heapq.heappop(q)
    if distance[now] < cost:
      continue
    if graph[now]:
      for i in graph[now]:
        if cost + i[1] < distance[i[0]]:
          distance[i[0]] = cost + i[1]
          heapq.heappush(q,(i[0],distance[i[0]]))
    if now < INF:
      if cost + 1 < distance[now+1]:
        distance[now+1] = cost + 1
    #   distance[now] = cost
        heapq.heappush(q,(now+1,cost+1))

for _ in range(n):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
di()
print(distance[d])