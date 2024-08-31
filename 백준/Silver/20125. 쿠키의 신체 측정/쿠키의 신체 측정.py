import sys

n = int(sys.stdin.readline())
pic = []
x_heart = 0
y_heart = 0
l_arm = 0
r_arm = 0
wrist = 0
l_leg = 0
r_leg = 0
for _ in range(n):
  tmp = sys.stdin.readline().strip()
  pic.append(tmp)
for i in range(1, len(pic)-1):
  for j in range(1, len(pic[i])-1):
    if pic[i-1][j] == '*' and pic[i+1][j] == '*' and pic[i][j-1] == '*' and pic[i][j+1] == '*':
      x_heart = i
      y_heart = j

for i in range(y_heart-1,-1,-1):
  if pic[x_heart][i] == '*':
    l_arm += 1
for i in range(y_heart+1,len(pic[0])):
  if pic[x_heart][i] == '*':
    r_arm += 1
for i in range(x_heart+1,n):
  if pic[i][y_heart] == '*':
    wrist += 1
for i in range(x_heart+wrist+1,n):
  if pic[i][y_heart-1] == '*':
    l_leg += 1
for i in range(x_heart+wrist+1,n):
  if pic[i][y_heart+1] == '*':
    r_leg += 1
print(x_heart+1, y_heart+1)
print(l_arm, r_arm, wrist, l_leg, r_leg)