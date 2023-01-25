import sys
P = []
T = int(input())
for i in range(T):
    P.append(sys.stdin.readline().rstrip('\n').split(' '))
for i in range(T):
    P[i][0] = int(P[i][0])
for i in range(T):
    for j in range(len(P[i][1])):
        print(P[i][0]*P[i][1][j],end ='')
    print()
