import sys
T = int(sys.stdin.readline())
for i in range(T):
    vps = sys.stdin.readline()
    sum = 0
    vps = list(vps)
    for j in vps:
        if j == '(':
            sum +=1
        elif j == ')':
            sum -=1
        if sum < 0:
            print('NO')
            break
    if sum >0:
        print('NO')
    elif sum == 0:
        print('YES')