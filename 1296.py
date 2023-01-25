man = input()
woman = []
per = []
for i in range(int(input())):
    woman.append(input())
woman.sort()

for w in woman:
    L = w.count('L') + man.count('L')
    O = w.count('O') + man.count('O')
    V = w.count('V') + man.count('V')
    E = w.count('E') + man.count('E')

    per.append(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)
print(woman[per.index(max(per))])