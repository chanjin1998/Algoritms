import sys

N,M= map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sum = 0
numRemainder = [0] * M

for i in range(N):
  sum += num[i]
  numRemainder[sum % M] += 1

result = numRemainder[0]

for i in numRemainder:
  result += i*(i-1)//2
  
print(result)

# M의 나머지 갯수만큼 배열을 만든 후 누적합의 나머지들이 몇개인지 각각 저장해준다. 나머지가 0인 곳은 result의 초깃값으로 저장 후 나머지가 같은 갯수의 2개를 뽑아 차를 구하면 나머지가 0이므로 그 구간까지 nC2로 더해준다.