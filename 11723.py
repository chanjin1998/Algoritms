import sys
s = set()
M = int(sys.stdin.readline())
for _ in range(M):
    inp = sys.stdin.readline().strip().split()
    if len(inp) == 1:
        if inp[0] == 'all':
            s = {x for x in range(1,21)}
        else:
            s = set()
        continue
    com = inp[0]
    target = int(inp[1])

    if com == 'add':
        s.add(target)
    elif com == 'remove':
        s.discard(target)
    elif com == 'check':
        if target in s:
            print(1)
        else:
            print(0)
    elif com == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)