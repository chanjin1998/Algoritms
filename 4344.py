import sys 
C = int(input())
data = []
for i in range(C):
    data.append(sys.stdin.readline().rstrip('\n').split(' '))
for j in range(C):
    data[j] = list(map(int,data[j]))

for k in range(C):
    sum = 0
    avg = 0
    count = 0
    for l in range(len(data[k])):
        sum += data[k][l]
    avg = (sum-data[k][0])/data[k][0]
    for i in range(len(data[k])):
        if i>=1 and avg<data[k][i]:
            count +=1
    print(format(count/data[k][0]*100,".3f")+'%')


            