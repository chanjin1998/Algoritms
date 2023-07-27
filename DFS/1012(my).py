import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())
def dfs(x, y):

  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if arr[x][y] == 0:
    # 해당 노드 방문 처리
    arr[x][y] = 1
    # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

for k in range(T):
  N, M, K = map(int, sys.stdin.readline().split())
  arr = [[1 for j in range(M)] for i in range(N)]
  for i in range(K):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 0

  result = 0
  for i in range(N):
    for j in range(M):
      # 현재 위치에서 DFS 수행
      if dfs(i, j) == True:
          result += 1

  print(result)  # 정답 출력