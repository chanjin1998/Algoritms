# b가 감염 => a 감염
# a가 감염 => b가 감염 x
import sys
import heapq

INF = int(1e9)
t = int(sys.stdin.readline())

def di(start):
  q = []
  heapq.heappush(q,(start,0))
  time[start] = 0
  cnt = 0
  while q:
    now, cost = heapq.heappop(q)
    if time[now] < cost:
      continue
    for i in graph[now]:
      if cost + i[1] < time[i[0]]:
        time[i[0]] = cost + i[1]
        heapq.heappush(q,(i[0],time[i[0]]))

for _ in range(t):
  n,d,com = map(int,sys.stdin.readline().split())
  total_time = 0
  total_cnt = 0
  graph = [[] for _ in range(n+1)]
  time = [INF for _ in range(n+1)]
  for _ in range(d):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[b].append((a,c))
  di(com)
  for val in time:
    if val != INF:
      total_cnt +=1
      if val > total_time:
        total_time = val
  print(total_cnt, total_time)
