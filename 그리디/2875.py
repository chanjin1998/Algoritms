import sys
N, M, K = map(int,sys.stdin.readline().split())
team = 0
while N>=2 and M>=1 and N+M>=K+3:
  N -= 2
  M -= 1
  team +=1
print(team)

# 여자에서 2명씩 뺴고 남자에서 1명씩 빼고 남녀가 인턴가는인원 + 3보다 크거나 같을 경우