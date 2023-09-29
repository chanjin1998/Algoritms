import sys
n = int(sys.stdin.readline())

def fac(n):
  if n == 1:
    return 1
  else:
    return n*fac(n-1)

print(fac(n)//(60*60*24*7))