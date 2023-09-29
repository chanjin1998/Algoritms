from itertools import combinations_with_replacement
import sys

n,m = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
li.sort()

for i in combinations_with_replacement(li,m):
  p = str(i)
  p = p.replace("(","").replace(",","").replace(")","")
  print(p)