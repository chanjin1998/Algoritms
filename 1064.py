N = int(input())
count = 0
for i in range(1,N+1):
    if i < 100:
        count +=1
    else:
        M = str(i)
        if int(M[0])-int(M[1]) == int(M[1])-int(M[2]):
            count +=1
print(count)
