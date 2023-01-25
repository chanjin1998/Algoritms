import sys
a,b = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())

record = [abs(int(sys.stdin.readline())-b) for i in range(n)]

print(min(abs(a-b), min(record)+1))
