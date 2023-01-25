import sys
A,B = map(int,sys.stdin.readline().split())
a = 0
for i in range(A,B+1):
    try:
        a ^= i
    except:
        break
print(a)

    