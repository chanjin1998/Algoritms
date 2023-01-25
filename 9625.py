import sys
k = int(sys.stdin.readline())
alpha = 'A'
result = ''
for i in range(k):
    for j in alpha:
        if j == 'A':
            result += 'B'
        elif j == 'B':
            result += 'BA'
    alpha = result
    if i == k-1:
        pass
    else:
        result=''
print(result.count('A'),result.count('B'))