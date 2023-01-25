import sys
N = int(sys.stdin.readline())
num = [0 for x in range(10)]
for i in str(N):
    num[int(i)] += 1
val = num[6]+num[9]
def ban(k):
    if k%2 == 0:
        return round((k//2))
    else:
        return round(k//2)+1
if val != 0:
    num[6] = 0
    num[9] = round(ban(int(val)))
print(max(num))
