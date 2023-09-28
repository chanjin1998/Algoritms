import sys
n = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
min_diff = int(1e9)

def back(dep,idx):
  global min_diff

  if dep == n//2:
    team_a = 0
    team_b = 0
    for i in range(n):
      for j in range(n):
        if visited[i] != 0 and visited[j] != 0:
          team_a += graph[i][j]
        elif visited[i] == 0 and visited[j] == 0:
          team_b += graph[i][j]
    min_diff = min(min_diff,abs(team_a-team_b))
    return
  for i in range(idx,n):
    if visited[i] == 0:
      visited[i] = 1
      back(dep+1,i+1)
      visited[i] = 0

back(0,0)
print(min_diff)