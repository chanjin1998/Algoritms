import sys
N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    a = sorted(lst,reverse=True)
    if max(lst) > sum(lst)//2:
        print('majority winner %d'%(lst.index(max(lst))+1))
    elif a[0] == a[1]:
        print('no winner')
    elif max(lst) <= sum(lst)//2:
        print('minority winner %d'%(lst.index(max(lst))+1))