from collections import deque
def solution(order):
    last = len(order)
    con = []
    car = []
    idx = 0
    n = 1
    while n < last + 2:
        # print(con)
        if con and con[-1] == order[idx]:
            car.append(con[-1])
            con.pop()
            idx += 1
        else:
            # print(n)
            con.append(n)
            n+=1
    return len(car)