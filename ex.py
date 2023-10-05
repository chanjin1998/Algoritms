from cmath import sqrt
import sys
import math
n = int(sys.stdin.readline())
a = int(pow(n,1/2))

val = []
for i in range(a,0,-1):
  ans = []
  res = 0
  while (True):
    if n == res:
      break
    if n-res >= pow(i,2):
      res += pow(i,2)
      ans.append(i)
    else:
      i -= 1
  val.append(len(ans))
print(min(val))
