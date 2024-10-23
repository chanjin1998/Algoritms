from collections import deque
def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
    def bfs(val):
        visited = [0 for _ in range(n+1)]
        q = deque()
        q.append(val)
        cnt = 1
        visited[val] = 1
        
        while q:
            node = q.popleft()
            for tmp in graph[node]:
                if visited[tmp] == 0:
                    q.append(tmp)
                    visited[tmp] = 1
                    cnt += 1
        return cnt
    res = n
    for wire in wires:
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        
        res = min(abs(bfs(wire[0])-bfs(wire[1])),res)
        
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
    return res