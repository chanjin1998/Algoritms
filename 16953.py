from collections import deque
import sys

a,b, = map(int,sys.stdin.readline().split())
q = deque()
q.append((a,1))

while q:
  num,cnt = q.popleft()
  if num > b:
    continue
  if num == b:
    print(cnt)
    break
  q.append((int(str(num)+'1'),cnt+1))
  q.append((num*2,cnt+1))
else:
  print(-1)