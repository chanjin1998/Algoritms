import sys
T = int(sys.stdin.readline())

def fibo(n):
    count0 = 0
    count1 = 0
    if n == 0:
        count0 +=1
        return 0
    elif n == 1:
        count1 +=1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
for i in range(T):
    a = int(sys.stdin.readline())
    print(fibo(a),count0)