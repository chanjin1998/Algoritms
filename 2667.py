from collections import deque
import sys

N = int(sys.stdin.readline())


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    global cnt
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # if graph[nx][ny] == 0:
            #     continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    # return cnt


graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 1
            bfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
