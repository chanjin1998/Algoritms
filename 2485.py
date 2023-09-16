import sys
from math import gcd
n = int(sys.stdin.readline())
f = int(sys.stdin.readline())
arr = []
for i in range(n-1):
  num = int(sys.stdin.readline())
  arr.append(num-f)
  f = num
g = arr[0]
for j in range(1,n-1):
  g = gcd(g,arr[j])
res = 0
for k in arr:
  res += k//g - 1
print(res)