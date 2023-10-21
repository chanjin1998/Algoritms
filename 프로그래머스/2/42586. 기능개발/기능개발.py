def solution(progresses, speeds):
    answer = []
    cnt = 0
    count = 0
    val = 0
    visited = [0 for _ in range(len(speeds))]
    while True:
        cnt +=1
        count = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                pass
            if progresses[i] < 100:
                progresses[i] += speeds[i]
            if progresses[0] >= 100 and visited[i] == 0:
                if progresses[val] >= 100:
                    val += 1
                    visited[i] = 1
                    count+=1
        if count!= 0:
            answer.append(count)
        print(progresses[0])
        if cnt == 100:
            break
    return answer