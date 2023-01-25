import sys
x,y,w,h = map(int,sys.stdin.readline().split())

answer = min(w-x,x,y,h-y)
print(answer)