A = []
for i in range(10):
    alpha = int(input())
    A.append(alpha%42)
A = set(A)
print(len(A))