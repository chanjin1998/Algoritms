import sys

# val1, val2 = sys.stdin.readline().split(' ')
x1 = int(input())
y1 = int(input())

if (x1>0 and y1>0):
    print(1)
elif (x1<0 and y1>0):
    print(2)
elif (x1<0 and y1<0):
    print(3)
elif (x1>0 and y1<0):
    print(4)

