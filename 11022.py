import sys

T = int(input())
list = []
for i in range(0,T):
    A, B = sys.stdin.readline().split(' ')
    A = int(A)
    B = int(B)
    list.append(A)
    list.append(B)
    list.append(A+B)
for i in range(1,T+1):
    print("Case #%d:"%(i),"%d + %d = %d"%(list[3*i-3],list[3*i-2],list[3*i-1]))