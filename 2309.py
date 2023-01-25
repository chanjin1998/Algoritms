import sys
nan = []
for i in range(9):
    nan.append(int(sys.stdin.readline()))
sum_s = sum(nan)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (nan[i] + nan[j]) == 100:
            one = nan[i]
            two = nan[j]
nan.remove(one)
nan.remove(two)
nan.sort()
for i in nan:
    print(i)