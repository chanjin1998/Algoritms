import sys

n, m = map(int, sys.stdin.readline().split())
memo = []

for _ in range(n):
    memo.append(sys.stdin.readline().rstrip())

print(memo)
blog = set()
for i in range(m):
    blog.add(str(sys.stdin.readline().rstrip().split(",")))
print(blog)
