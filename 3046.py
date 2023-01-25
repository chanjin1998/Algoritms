import sys
R1,S = map(int,sys.stdin.readline().split())
if R1 > S:
    print(S-(R1-S))
elif R1 < S:
    print(S+(S-R1))
else:
    print(S)