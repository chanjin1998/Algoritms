def solution(m, n, puddles):
    answer = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for water in puddles:
        visited[water[1]-1][water[0]-1] = 1
        
    for i in range(m):
        if visited[0][i] == 0:
            dp[0][i] = 1
            
        else:
            for j in range(i,m):
                dp[0][j] = 0
                break
            break
    for i in range(n):
        if visited[i][0] == 1:
            for j in range(i,n):
                dp[i][0] = 0
                break
            break
        else:
            dp[i][0] = 1
    
    for j in range(n):
        for i in range(m):
            if i != 0 and j != 0 and visited[j][i] == 0:
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
            elif visited[j][i] == 1:
                dp[j][i] = 0
    return dp[n-1][m-1]%1000000007
    # return dp
# 1 0 0 0
# 1 1 1 1
# 1 2 3 4