N = int(input())

count = 0
x = 1
i = -1
while (N>=x):
    i+=1
    x +=6*i
    if N <= x:
        count = i+1
        break
print(count)