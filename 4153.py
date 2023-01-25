import sys
while (1):
    tri = list(map(int,sys.stdin.readline().split()))
    tri.sort()
    a = tri[0]
    b = tri[1]
    c = tri[2]
    if a == 0 and b ==0 and c ==0:
        break
    elif pow(a,2)+pow(b,2) == pow(c,2):
        print('right')
    else:
        print('wrong')