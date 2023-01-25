import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    order_sen = sys.stdin.readline().split()
    order = order_sen[0]
    if order == 'push':
        stack.append(int(order_sen[1]))
    elif order == 'top':
        if len(stack) !=0:
            print(stack[-1])
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) != 0:
            print(0)
        else: 
            print(1)
    elif order == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
