n = input()
val = ''
for i in n:
    if i.islower():
        val += i.upper()
    else:
        val += i.lower()
print(val)