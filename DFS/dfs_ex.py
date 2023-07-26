from collections import deque

# DFS(Depth First Search) : 깊이 우선 탐색
# 그래프 깊은 부분부터 우선적으로 탐색하는 알고리즘
# 스택 자료구조 이용, 재귀함수 이용
# 그래프 - 노드 & 간선으로 표현
# 인접 행렬 : 2차월 배열로 그래프의 연결 관계를 표현
# 인접 리스트 : 리스트로 그래프의 연결 관계를 표현

def dfs(graph, v, visited):
  visited[v] = True
  print(v,end='')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
    [],
    [2,3,7],
    [1,4,6],
    [1,5, 7],
    [2,6],
    [3,7],
    [2,4],
    [1,3]
]

#각 노드가 방문한 정보를 리스트 자료형으로 표현
visited = [False] * 9

print("방문순서")
dfs(graph, 1, visited)