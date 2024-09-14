import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
sum_val = 0
min_val = 0
for i in range(m,n+1):
  if pow(i,0.5) == int(pow(i,0.5)):
    if sum_val == 0:
      min_val = i
    sum_val += i

if min_val == 0:
  print(-1)
else:
  print(sum_val)
  print(min_val)    