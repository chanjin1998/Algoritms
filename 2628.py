import sys
a,b = map(int,sys.stdin.readline().split())
s = int(sys.stdin.readline())
width = []
wid_val = []
height = []
hei_val = []
for i in range(s):
    val,alpha = map(int,sys.stdin.readline().split())
    if val == 0:
        width.append(alpha)
    else:
        height.append(alpha)
width.sort()
height.sort()
if len(width) == 1:
    wid_val.append(max(width[0],b-width[0]))
elif len(width) >1:   
    for i in range(len(width)-1):
        wid_val.append((width[i+1]-width[i]))
    wid_val.append(width[0])
    wid_val.append(b-width[-1])
else:
    wid_val.append(b)
if len(height) == 1:
    hei_val.append(max(height[0],a-height[0]))
elif len(height)>1:   
    for i in range(len(height)-1):
        hei_val.append((height[i+1]-height[i]))
    hei_val.append(max(height[0],a-height[-1]))
else:
    hei_val.append(a)
print(max(wid_val)*max(hei_val))