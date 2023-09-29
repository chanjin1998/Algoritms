from itertools import permutations
import sys

n,m = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
li.sort()

res = []
for i in permutations(li,m):
  p = str(i)
  # p = p.replace("(","").replace(",","").replace(")","")
  res.append(p)
res = set(res)
res = list(res)
res.sort()
for i in res:
  print(i)