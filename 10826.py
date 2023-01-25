# import sys
# n = int(sys.stdin.readline())
# def fivo(k):
#     if k == 0:
#         return 0
#     elif k == 1:
#         return 1
#     else:
#         return fivo(k-1)+fivo(k-2)
# print(fivo(n))
n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a+b
print(a)