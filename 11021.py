import sys
list = []
val = int(input())
for i in range(1,val+1):
    val1, val2 = map(int,sys.stdin.readline().split(' '))
    list.append(val1+val2)
for i in range(0,val):
    print("Case #%d:"%(i+1),list[i])