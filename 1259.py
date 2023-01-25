# import sys
# while (1):
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break
#     n = str(n)
#     if (len(n) % 2) == 0:
#         for i in range(len(n)//2):
#             if str(n)[i] != str(n)[len(n)-1-i]:
#                 print('no')
#                 break
#             if i == len(n)/2 - 1:
#                 print('yes')
    
#     else:
#         for j in range(len(n)//2):
#             if str(n)[j] != str(n)[len(n)-1-j]:
#                 print('no')
#                 break
#             if j == len(n)//2 -1:
#                 print('yes')
while (1):
    n = input()
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')