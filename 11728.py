import sys
n = int(sys.stdin.readline())
cnt = 0
if n ==1 or n ==3:
    cnt = -1
elif n % 5 ==0:
    cnt += n // 5
elif (n - (n//5)*5)%2 ==0:
    cnt += n // 5
    n = n - 5*(cnt)
    cnt += n //2
elif (n - (n//5)*5)%2 !=0:
    cnt += (n // 5)-1
    n = n - 5*cnt
    cnt += n // 2

print(cnt)