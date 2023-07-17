import sys
N = int(sys.stdin.readline())
ball = sys.stdin.readline()
red = ball.rstrip().split('B')
blue = ball.rstrip().split('R')
cnt = 0
# for i in range(1,N):
#   if ball[i] != ball[i-1]:
#     cnt += 1

print(red)
print(blue)