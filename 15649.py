import sys
N, M = map(int,sys.stdin.readline().split())
visited = [False] * N
res = []

def solve(depth,cnt, N, M):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for i in range(cnt,len(visited)): 
        if not visited[i]:
            visited[i] = True
            res.append(i+1)  
            solve(depth+1,i, N, M)
            visited[i] = False
            res.pop()

solve(0,0, N, M)