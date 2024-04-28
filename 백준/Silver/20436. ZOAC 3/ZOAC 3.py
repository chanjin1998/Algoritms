import sys
l,r = map(str,sys.stdin.readline().split())
l_group = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v']
r_group = ['y','u','i','o','p','h','j','k','l','b','n','m']
time = 0
l_val = [[0,2],[1,2],[2,2],[3,2],[4,2],[0,1],[1,1],[2,1],[3,1],[4,1],[0,0],[1,0],[2,0],[3,0]]
r_val = [[5,2],[6,2],[7,2],[8,2],[9,2],[5,1],[6,1],[7,1],[8,1],[4,0],[5,0],[6,0]]
words = sys.stdin.readline().strip()
for word in words:
  if word in l_group:
    l_bef = l_group.index(l)
    bef_x = l_val[l_bef][0]
    bef_y = l_val[l_bef][1]
    l = word
    l_aft = l_group.index(l)
    aft_x = l_val[l_aft][0]
    aft_y = l_val[l_aft][1]
    time += abs(aft_x-bef_x) + abs(aft_y-bef_y) + 1
  elif word in r_group:
    r_bef = r_group.index(r)
    bef_x = r_val[r_bef][0]
    bef_y = r_val[r_bef][1]
    r = word
    r_aft = r_group.index(r)
    aft_x = r_val[r_aft][0]
    aft_y = r_val[r_aft][1]
    time += abs(aft_x-bef_x) + abs(aft_y-bef_y) + 1
print(time)