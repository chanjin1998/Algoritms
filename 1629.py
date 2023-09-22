import sys

n,m,c = map(int,sys.stdin.readline().split())

def recur(m,n,c):
  if n == 1:
    return m % c
  elif n % 2 == 0:
    res = recur(m,n/2,c)
    return res * res%c
  else:
    res = recur(m,(n-1)/2,c)
    return res*res*m%c
print(recur(n,m,c))