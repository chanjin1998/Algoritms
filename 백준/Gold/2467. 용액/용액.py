import sys
input = sys.stdin.readline

n = int(input())
fluid = list(map(int, input().split()))

left = 0
right = n - 1

ans = abs(fluid[left] + fluid[right])
ans_left = left
ans_right = right

while left < right:
    tmp = fluid[left] + fluid[right]

    if abs(tmp) < ans:
        ans_left = left
        ans_right = right
        ans = abs(tmp)

        if ans == 0:
            break
    
    if tmp < 0:
        left += 1
    
    else:
        right -= 1

print(fluid[ans_left], fluid[ans_right])