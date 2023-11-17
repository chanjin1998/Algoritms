from collections import deque
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i+1].append(j+1)
    q = deque()
    cnt = 1
    for k in range(1,n+1):
        if visited[k] == 0:
            q.append(k)
            while q:
                alpha = q.popleft()
                for i in graph[alpha]:
                    if visited[i] == 0:
                        q.append(i)
                        visited[i] = cnt
            cnt += 1
        
    return cnt - 1