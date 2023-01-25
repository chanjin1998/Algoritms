arr = input().split('-')
a = 0
for i in arr[0].split('+'):
    a += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        a -= int(j)
print(a)