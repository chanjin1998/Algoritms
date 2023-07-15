import sys
N = int(sys.stdin.readline())
drink = list(map(int,sys.stdin.readline().split()))
drink.sort()
cnt = 0
for i in range(N-1):
  # if cnt > drink[i+1]:
  #   cnt += drink[i+1]/2
  # else:
  #   cnt = cnt/2 + drink[i+1]
  cnt += drink[i]/2
num = cnt+drink[-1]
print(num)
