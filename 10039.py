import sys

sum = 0
for _ in range(5):
    a = int(sys.stdin.readline().rstrip())
    if a<40:
      sum += 40
    else:
      sum += a
print(int(sum / 5))
