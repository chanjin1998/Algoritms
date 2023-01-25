import sys
a = []
for i in range(9):
    val = int(input())
    a.append(val)
a = list(a)
max = a[0]
for i in range(9):
    if max<a[i]:
        max = a[i]
A = a.index(max)
print(max)
print(A+1)