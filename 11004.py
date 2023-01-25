import sys
n = int(sys.stdin.readline())
cnt = 0
val = {}
for _ in range(n):
    a = sys.stdin.readline().split()
    val[a[0]] = a[1]
def get_key():
    res = []
    for key,value in val.items():
        if value == 'enter':
            res.append()
print(get_key())