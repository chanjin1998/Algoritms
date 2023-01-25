import sys
n = int(sys.stdin.readline())
a,b = 0,1
fivo = [0 for x in range(n)]

for i in range(n):
    a,b = b,a+b
    fivo[i] = a

def mat(n):
    if n == 1:
        return 4
    elif n == 2:
        return 6
    elif n == 3:
        return 10
    else:
        return fivo[-1]*3+fivo[-2]*2+fivo[-3]*2+fivo[-4]
print(mat(n))