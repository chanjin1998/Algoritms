import sys
N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
res = list(map(int,sys.stdin.readline().split()))
num.sort()
for i in res:
    start = 0
    end = len(num)-1
    answer = 0
    
    while start <= end:
        mid = (start + end)//2
        if num[mid] == i:
            answer = 1
            break
        elif num[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    print(answer , end = ' ')