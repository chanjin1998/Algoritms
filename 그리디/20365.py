import sys
N = int(sys.stdin.readline())
color = sys.stdin.readline()

color_dic = {'B':0 , 'R':0}
color_dic[color[0]] += 1
for i in range(1,N):
  if color[i] != color[i-1]:
    color_dic[color[i]] += 1
cnt = min(color_dic['B'],color_dic['R']) + 1

print(cnt)