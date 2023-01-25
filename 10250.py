import sys
# H=높이 W=너비 N=손님수 
T = int(input())
val = []
for i in range(T):
    H, W, N = map(int,sys.stdin.readline().split())
    if N % H != 0:
        room_floor = N % H
        room_num = (N // H) +1
    else:
        room_floor = H
        room_num = (N // H)
    if room_num<10:
        room_name = '%d0%d'%(room_floor,room_num)
    elif room_num>=10:
        room_name = '%d%d'%(room_floor,room_num)
    val.append(int(room_name))
for i in range(T):
    print(val[i])

    