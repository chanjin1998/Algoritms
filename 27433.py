import sys

n = int(sys.stdin.readline())

def fac(n):
  if n >= 2:
    return n * fac(n-1)
  else:
    return 1
print(fac(n))