import sys
n = int(sys.stdin.readline())
tree = list(map(int,sys.stdin.readline().split()))
val = [0 for x in range(len(tree))]
tree.sort(reverse = True)
for i in range(1,len(tree)+1):
    val[i-1] = i+tree[i-1]
print(max(val)+1)