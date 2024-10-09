import sys

N,M = map(int,sys.stdin.readline().split())
cookie = dict()
for _ in range(N+M):
  site = list(map(str,sys.stdin.readline().split()))
  if len(site) == 2:
    cookie[site[0]] = site[1]
  else:
    print(cookie[site[0]])