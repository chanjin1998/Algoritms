import sys

def change(a,b):
    temp = []
    while a > 0:
        temp.append(a%b)
        a //= b
    temp = temp[::-1]
    return temp
def check(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
t = int(sys.stdin.readline())
for j in range(t):
    cnt = False
    n = int(sys.stdin.readline())
    for i in range(2,65):
        if check(change(n,i)):
            cnt = check(change(n,i))
            break
    if cnt:
        print(1)
    else:
        print(0)