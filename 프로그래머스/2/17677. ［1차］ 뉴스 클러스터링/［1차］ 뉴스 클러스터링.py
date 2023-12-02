import math
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str1_li = []
    str2 = str2.upper()
    str2_li = []
    for i in range(len(str1)-1):
        if 65<=ord(str1[i])<=90 and 65<=ord(str1[i+1])<=90:
            str1_li.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if 65<=ord(str2[i])<=90 and 65<=ord(str2[i+1])<=90:
            str2_li.append(str2[i]+str2[i+1])

    a1 = str1_li.copy()
    a2 = str1_li.copy()
    for i in str2_li:
        if i not in a1:
            a2.append(i)
        else:
            a1.remove(i)
    common = []
    for i in str2_li:
        if i in str1_li:
            str1_li.remove(i)
            common.append(i)
    print(a2)
    print(common)
    if len(a2) == 0 and len(common) == 0:
        return 65536
    else:
        return math.trunc(len(common)/len(a2)*65536)
    # aa aa ,aa aa aa