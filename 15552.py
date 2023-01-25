import sys
res_list=[]
T = int(sys.stdin.readline())
for i in range(0,T):
    a,b = map(int,sys.stdin.readline().split())
    res_list.append(a+b)
for i in range(0,T):
    print(res_list[i])