import sys
a,b,c = map(int,sys.stdin.readline().split())
e, s, m, cnt = 0,0,0,0
while(1):
    e+=1
    s+=1
    m+=1
    cnt +=1
    if e % 16 == 0:
        e = 1
    if s % 29 == 0:
        s = 1
    if m % 20 == 0:
        m = 1
    if a==e and b ==s and c == m:
        break
print(cnt)