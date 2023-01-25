import sys
a=[]
N = int(input())
for i in range(N):
    a.append(sys.stdin.readline().rstrip('\n'))
for i in range(N):
    count = 0
    Vcount = 0
    for j in range(len(a[i])):
        if (a[i][j]=='O'):
            count +=1
            count += Vcount
            try:
                if a[i][j] == a[i][j+1]:
                    Vcount +=1
            except:
                Vcount = 0
        else :
            Vcount = 0
    print(count)
