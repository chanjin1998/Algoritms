import sys
N = int(sys.stdin.readline())
card = [x for x in range(1,N+1)]
res = []
while len(card)>=2:
    res.append(card[0])
    card.append(card[1])
    del card[0]
    del card[0]
res.append(card[0])
for j in range(len(res)):
    print(res[j],end=' ')