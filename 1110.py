N = int(input())
A = N
cnt = 0
while (1):
    if A < 10:
        A = A*11
        cnt +=1
    elif A >=10:
        tenVal = A//10
        oneVal = A%10
        if (tenVal+oneVal)<10:
            A = oneVal * 10 + tenVal+oneVal
            cnt +=1
        elif (tenVal+oneVal)>=10:
            newVal = (tenVal+oneVal)%10
            A = oneVal*10 + newVal
            cnt+=1
    if A == N:
        break
print(cnt)
    