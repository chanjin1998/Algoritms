def solution(triangle):
    answer = 0
    height = len(triangle)
    visited = [[] for _ in range(height)]
    for i in range(height):
        for j in range(i+1):
            visited[i].append(0)
    visited[0][0] = triangle[0][0]
    visited[1][0] = visited[0][0] + triangle[1][0]
    visited[1][1] = visited[0][0] + triangle[1][1]
    
    for i in range(2,height):
        for j in range(i+1): #0,1,2
            if j == 0:
                visited[i][j] = visited[i-1][j] + triangle[i][j]
            elif j == i:
                visited[i][j] = visited[i-1][j-1] + triangle[i][j]
            else:
                visited[i][j] = max(visited[i-1][j-1],visited[i-1][j]) + triangle[i][j]
    return max(visited[height-1])