import sys
k = int(sys.stdin.readline())
for i in range(k):
    sEt = list(map(int,sys.stdin.readline().split()))
    del sEt[0]
    sEt.sort()
    res = []
    for k in range(len(sEt)-1): 
        res.append(sEt[k+1]-sEt[k])
    print('Class %d'%(i+1))
    print('Max %d, Min %d, Largest gap %d'%(max(sEt),min(sEt),max(res)))