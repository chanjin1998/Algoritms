word = list(input())
answer = []
tmp = []

for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a+b+c)
for k in tmp:
    answer.append(''.join(k))
print(sorted(answer)[0])