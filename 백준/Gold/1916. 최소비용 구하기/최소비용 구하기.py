import sys
import heapq

INF = int(1e9)
def di(start):
  q = []
  heapq.heappush(q,(start,0))
  
  while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
      if now == end:
        break
      else:
        continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(i[0],cost))
  
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
distance = [ INF for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
start, end = map(int,sys.stdin.readline().split())
di(start)
print(distance[end])
