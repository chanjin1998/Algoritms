S = input()

for j in range(97,123):
    if chr(j) in S:
        val = S.find(chr(j))
        print(val, end=' ')
    else:
        print(-1,end=' ')
            
