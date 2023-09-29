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