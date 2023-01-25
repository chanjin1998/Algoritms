import sys
N = int(sys.stdin.readline())
q = []

for i in range(N):
    val = sys.stdin.readline().split()

    if val[0] == "push":
        q.insert(0, val[1])

    elif val[0] == "pop":
        if len(q) != 0: print(q.pop())
        else: print(-1)

    elif val[0] == "size":
        print(len(q))

    elif val[0] == "empty":
        if len(q) == 0: print(1)
        else : print(0)

    elif val[0] == "front":
        if len(q) == 0: print(-1)
        else: print(q[len(q) -1])

    elif val[0] == "back":
        if len(q) == 0: print(-1)
        else: print(q[0])