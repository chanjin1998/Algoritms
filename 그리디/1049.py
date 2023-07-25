import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

minSix = 1001
minSingle = 1001
for i in range(M):
  p, s = map(int, input().split(' '))
  minSix = min(minSix, p)
  minSingle = min(minSingle, s)

result = 0

if minSix > minSingle*6:
  result += N * minSingle
else:
  result += (N//6) * minSix

  if (N%6)*minSingle > minSix:
    result += minSix
  else:
    result+= (N%6)*minSingle

print(result)