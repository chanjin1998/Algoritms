<<<<<<< HEAD
from itertools import combinations
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
li = deque()
for i in range(1,n+1):
  li.append(i)
a = deque()
a = deque(combinations(li,m))
print(a)
=======
import sys
n,m = map(int,sys.stdin.readline().split())
arr = []
for i in range(1,n+1):
  if n % i == 0:
    arr.append(i)
try:
  print(arr[m-1])
except:
  print(0)
>>>>>>> parent of d283db6 (파일 정리)
