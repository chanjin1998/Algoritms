import sys

a,b,c = sys.stdin.readline().split(' ')
dice1 = int(a)
dice2 = int(b)
dice3 = int(c)
numbers = [dice1,dice2,dice3]
new_num = sorted(numbers)
val1 = new_num[0]
val2 = new_num[1]
val3 = new_num[2]

if (val1==val2==val3):
    price = 10000 + dice1*1000
elif ((val1==val2 and val1!=val3)or(val2==val3 and val1!=val3)):
    price = 1000 + val2*100
elif (val1!=val2 and val1!=val3 and val2!=val3):
    price = val3*100

print(price)