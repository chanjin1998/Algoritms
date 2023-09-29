import sys
day = int(sys.stdin.readline())
time = [1]*22
pay = [0] * 22
res = []
for i in range(1,day+1):
  a,b = map(int,sys.stdin.readline().split())
  time[i] = a
  pay[i] = b

for i in range(1,day+1):
  new_day = i
  new_pay = 0
  while (time[new_day] + new_day <= day+1):
    # print(0)
    # if time[new_day] + new_day <8:
    new_pay += pay[new_day]
    new_day = new_day + time[new_day]
    print(new_day,new_pay)
  res.append(new_pay)
print(max(res))