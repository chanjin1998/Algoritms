N = int(input())
val = []
a = ''
for i in str(N):
    val.append(i)
val.sort(reverse=True)
for j in range(len(val)):
    a += val[j]
print(a)