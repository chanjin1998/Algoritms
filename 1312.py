import sys
a,b,n = map(int,sys.stdin.readline().split())
try:
    if b != 0:
        val = str(a/b)
        c = val.index('.')
        print(val[c+n])
finally:
    a = 1