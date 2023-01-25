import sys
K = int(sys.stdin.readline())
money = []
for i in range(K):
    a = (int(sys.stdin.readline()))
    if a == 0:
        del money[-1]
    else:
        money.append(a)
print(sum(money))