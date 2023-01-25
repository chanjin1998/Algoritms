import sys

h, m = sys.stdin.readline().split(' ')
hour = int(h)
min = int(m)

if (hour != 0 and min<45):
    print(hour-1, min+15)
elif (hour ==0 and min<45):
    print(hour+23, min+15)
else:
    print(hour,min-45)