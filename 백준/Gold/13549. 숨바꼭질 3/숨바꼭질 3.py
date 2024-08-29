import sys
import heapq
INF = int(1e5)

n, k = map(int,sys.stdin.readline().split())
distance = [ INF for _ in range(INF+1)]
distance[n] = 0
def di(start):
  q = []
  heapq.heappush(q,(start,0))
  while q:
    now, time = heapq.heappop(q)
    if distance[now] < time:
      continue
    if now + 1< INF+1:
      if time + 1 < distance[now+1]:
        distance[now+1] = time + 1
        heapq.heappush(q,(now+1, time+1))
    if now - 1 >= 0:
      if time + 1 < distance[now-1]:
        distance[now-1] = time + 1
        heapq.heappush(q,(now-1, time+1))
    if now * 2 < INF+1:
        if time < distance[now*2]:
            distance[now*2] = time
            heapq.heappush(q,(now*2, time))

di(n)
print(distance[k])