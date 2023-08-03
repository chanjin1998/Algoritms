import sys
n = int(sys.stdin.readline())
cost = []
cost = list(map(int,sys.stdin.readline().split()))
cost.sort()
print(cost)