import sys
N = int(sys.stdin.readline())
for i in range(N):
  q= 0
  d=0
  n=0
  p=0
  change = int(sys.stdin.readline())
  if change//25 != 0:
    q = change//25
    change %= 25
  if change//10 !=0:
    d = change//10
    change %= 10
  if change//5 !=0:
    n = change//5
    change %= 5
  if change//1 !=0:
    p = change//1
  print(q,d,n,p,end='')
  print()