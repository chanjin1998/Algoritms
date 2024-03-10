import sys
x, y = map(int,sys.stdin.readline().split())
days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
num = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 0
for i in range(0,x-1):
    day += num[i]
day = (day + y)%7
print(days[day])
#print
#print