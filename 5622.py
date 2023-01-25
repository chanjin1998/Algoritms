word = input()
W_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
count = 0
for i in range(len(word)):
    for j in W_list:
        if word[i] in j:
            count += W_list.index(j) + 3

print(count)