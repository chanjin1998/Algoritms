N = int(input()) #9
x = 0 # 번호
i = 0 # 라인
while (N>x):
    i += 1
    x += i
if i % 2 ==0:
    print('%d/%d' % (i-x+N,1+x-N))
else:
    print('%d/%d' % (1+x-N,i-x+N))

        