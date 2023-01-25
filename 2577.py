from re import L
import sys

V = 1
for i in range(3):
    A = int(input())
    V = A * V

V = str(V)
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt9 = 0
for i in range(len(V)):
    if V[i] == '0':
        cnt +=1
    elif V[i] =='1':
        cnt1 +=1
    elif V[i] =='2':
        cnt2 +=1
    elif V[i] =='3':
        cnt3 +=1
    elif V[i] =='4':
        cnt4 +=1
    elif V[i] =='5':
        cnt5 +=1
    elif V[i] =='6':
        cnt6 +=1
    elif V[i] =='7':
        cnt7 +=1
    elif V[i] =='8':
        cnt8 +=1
    elif V[i] =='9':
        cnt9 +=1
print(cnt)
print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)
print(cnt5)
print(cnt6)
print(cnt7)
print(cnt8)
print(cnt9)