import sys
x = sys.stdin.readline()
cnt = 0
while (x>9):
    y = 0
    for i in range(len(x)):
        y += int(x[i])
    cnt +=1
    x = y
if x % 3 == 0:
    print(cnt)
    print('YES')
else:
    print(cnt)
    print('NO')