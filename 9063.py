import sys
n = int(sys.stdin.readline())
x = []
y = []
for i in range(n):
  a,b = map(int,sys.stdin.readline().split())
  x.append(a)
  y.append(b)
x.sort()
y.sort()
val = (x[-1]-x[0])*(y[-1]-y[0])
try:
  print(val)
except:
  print(0)