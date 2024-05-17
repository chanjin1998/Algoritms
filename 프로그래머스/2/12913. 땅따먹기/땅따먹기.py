import copy
def solution(land):
    answer = 0
    h = len(land)
    w = len(land[0])
    visited = [[0 for _ in range(w)] for _ in range(h)]
    graph = copy.deepcopy(land)

    for i in range(1,h):
        max_val = 0
        for j in range(4):
            if j == 0:
                max_val = max(graph[i-1][1],graph[i-1][2],graph[i-1][3])
            elif j == 1:
                max_val = max(graph[i-1][0],graph[i-1][2],graph[i-1][3])
            elif j == 2:
                max_val = max(graph[i-1][0],graph[i-1][1],graph[i-1][3])
            else:
                max_val = max(graph[i-1][1],graph[i-1][2],graph[i-1][0])
            graph[i][j] += max_val
    return max(graph[h-1])