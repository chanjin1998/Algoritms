import sys
a_num = 0
cnt = 0
val = []
a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
res = list(map(int,sys.stdin.readline().split()))
for i in range(m):
    a_num += pow(a,i)*res[m-1-i]
alpha = a_num
while (alpha>=b):
    alpha = alpha // b
    cnt +=1
for j in range(cnt,-1,-1):
    if j != 0:
        val.append(str(a_num//pow(b,cnt)))
        a_num = a_num % pow(b,cnt)
    else:
        val.append(str(a_num))
fin = ' '.join(val)
print(fin)