import math
import sys
def four_squares(n):

  if int(math.sqrt(n)) == math.sqrt(n):
    return 1

  for i in range(1, int(math.sqrt(n)) + 1):

    if int(math.sqrt(n - pow(i, 2))) == math.sqrt(n - pow(i, 2)):
      return 2

  for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - pow(i,2))) + 1):
            if int(math.sqrt(n - pow(i,2) - pow(j,2))) == math.sqrt(n - pow(i,2) - pow(j,2)):
                return 3

  return 4

n = int(sys.stdin.readline())
print(four_squares(n))