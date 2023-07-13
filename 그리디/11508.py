import sys
N = int(sys.stdin.readline())
num = []
price = 0
for i in range(N):
  num.append(int(sys.stdin.readline().rstrip()))
num.sort(reverse=True)
for i in range(N):
  if (i+1)%3 != 0:
    price += num[i]
  else:
    pass
print(price)