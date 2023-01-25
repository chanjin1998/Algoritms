import sys

N, k = map(int,sys.stdin.readline().split())
score = []
a = list(map(int,sys.stdin.readline().split()))
a.sort(reverse = True)
print(a[k-1])