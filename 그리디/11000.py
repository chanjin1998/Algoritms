import sys
N = int(sys.stdin.readline())
lec = []
cnt=0
for i in range(N):
  lec.append(list((map(int,sys.stdin.readline().split()))))
lec.sort()
for i in range(N-1):
  if lec[i][1]<=lec[i+1][0]:
    pass
  else:
    cnt+=1
print(cnt)