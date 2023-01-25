word = input()
alpha = ['dz=','lj','nj','c=','c-','d-','s=','z=']
count = 0
for i in alpha:
    if i in word:
        count+=1
print(word)
print(len(word)-count)