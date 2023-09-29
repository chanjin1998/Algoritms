from collections import deque
import sys

n = int(sys.stdin.readline())
w1, w2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

q = deque()
q.append(w1)
visited[w1] = 0
while q:
    alpha = q.popleft()
    if alpha == w2:
        break
    for nx in graph[alpha]:
        if visited[nx] == 0:
            visited[nx] = visited[alpha]+1
            q.append(nx)
else:
  visited[w2] = -1
print(visited[w2])
