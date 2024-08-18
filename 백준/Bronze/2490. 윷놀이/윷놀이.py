import sys

for i in range(3):
  a,b,c,d = map(int,sys.stdin.readline().split())
  cnt = a+b+c+d
  if cnt == 0:
    print("D")
  elif cnt == 4:
    print("E")
  elif cnt == 2:
    print("B")
  elif cnt == 3:
    print("A")
  elif cnt == 1:
    print("C")