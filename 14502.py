from collections import deque
from itertools import combinations
import sys
import copy

n, m = map(int, sys.stdin.readline().split())
graph = []
res = []

def get_count(graph1):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph1[i][j] == 0:
                cnt += 1
    return cnt

def bfs():
    graph1 = copy.deepcopy(graph) # 그래프를 깊은 복사로 계속 새 그래프로 만듦
    visited = [[0 for _ in range(m)] for _ in range(n)] # 방문 노드도 새로 만들어줌
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque() # 2인 값을 찾아서 큐에 넣어줌
    for i in range(n):
        for j in range(m):
            if graph1[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph1[nx][ny] == 0 and visited[nx][ny] == 0:
                    graph1[nx][ny] = 2
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    res.append(get_count(graph1)) # 새로 만들어진 그래프의 0의 갯수를 출력하기 위해

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            q.append((i, j))
a = deque(combinations(q, 3)) # 0인값의 좌표를 큐에 넣어준 후 3개씩 조합으로 뽑아줌
for i in a:
    for j in i:
        graph[j[0]][j[1]] = 1 # 3개씩 뽑은 것중 0을 1로 교체
    bfs()
    for j in i:
        graph[j[0]][j[1]] = 0 # 1로 바뀐것들을 0으로 교체

print(max(res))