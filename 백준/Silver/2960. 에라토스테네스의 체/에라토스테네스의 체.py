import sys
import math
n,k = map(int,sys.stdin.readline().split())
check = [True for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0
val = 0
for i in range(2,n+1):
  if check[i] == True:
    visited[i] = 1
    cnt += 1
    j = 2
    if cnt == k:
      val = i
    while (i*j<=n):
      if visited[i*j] == 0:
        visited[i*j] = 1
        check[i*j] = False
        cnt += 1
        if cnt == k:
          val = i*j
      j += 1
print(val)