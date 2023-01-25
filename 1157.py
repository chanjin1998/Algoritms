W = input()
W = W.upper()

W_list = list(set(W))
cnt = []

for i in W_list:
    count = W.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >=2 :
    print("?")
else:
    print(W_list[(cnt.index(max(cnt)))])