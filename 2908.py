from random import betavariate
import sys

num1, num2 = map(str,sys.stdin.readline().split())
l1 = list(num1)
alpha = l1[0]
l1[0] = l1[2]
l1[2] = alpha
l2 = list(num2)
beta = l2[0]
l2[0] = l2[2]
l2[2] = beta
s1 = "".join(l1)
s2 = "".join(l2)
if s1>s2:
    print(s1)
elif s1<s2:
    print(s2)