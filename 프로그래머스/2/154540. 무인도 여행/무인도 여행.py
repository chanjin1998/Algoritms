from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    graph = []
    result = []
    for i in maps:
        graph.append(list(i))
    # print(graph)
    def bfs(j,i):
        cnt = 0
        q = deque()
        q.append((j,i)) # x,y
        cnt += int(graph[i][j])
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        # cnt += gra
        while q:
            x,y = q.popleft()
            visited[y][x] = 1
            # cnt += int(graph[y][x])
            # print(int(graph[y][x]))
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0<=nx<m and 0<=ny<n:
                    if visited[ny][nx] == 0 and graph[ny][nx] != 'X':
                        visited[ny][nx] = 1
                        q.append((nx,ny))
                        cnt += int(graph[ny][nx])
        return cnt
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 'X' and visited[i][j] == 0:
                a = bfs(j,i) #x,y
                result.append(a)
                result.sort()
    if len(result) == 0:
        result.append(-1)
    return result


