import sys

a,b = sys.stdin.readline().split(' ')
c = sys.stdin.readline()
hour = int(a)
min = int(b)
cook_min = int(c)

if (min+cook_min>=60):
    add_hour = (min+cook_min)//60
    add_min = (min+cook_min)%60
    if (hour+add_hour>=24):
        print(hour+add_hour-24,add_min)
    else:
        print(hour+add_hour, add_min)
else:
    print(hour,min+cook_min)