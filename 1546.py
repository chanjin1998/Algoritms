import sys

score = []
newScore = []
N = int(input())
score = map(int,sys.stdin.readline().split(' '))
score = list(score)
max = 0
sum = 0
for i in range(len(score)):
    if (score[i]>max):
        max = score[i]
for j in range(len(score)):
    newScore.append(score[j]/max*100)
for k in range(len(newScore)):
    sum += newScore[k]
print(sum/N)