import sys
a = int(sys.stdin.readline())
x = 1
while x*(x+1)/2 <= a:
    x+=1
print(x-1)