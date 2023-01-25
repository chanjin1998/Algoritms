N = int(input())
val = {}
for i in range(1,1000001):
    k = str(i)
    a= i
    for j in k:
        i += int(j)
    val[a] = i

key = list(val.keys())
value = list(val.values())
if N in value:
    position = value.index(N)
    print(key[position])
else:
    print(0)