n = int(input())

fivo = [0,1]
for i in range(2,n+1):
    fivo.append(fivo[i-2] + fivo[i-1])
print(fivo[n])