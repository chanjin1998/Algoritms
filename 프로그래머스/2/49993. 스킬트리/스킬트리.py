def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        tmp = 0
        check = 0
        for tree in skill_tree:
            if tree in skill:
                check += 1
            if tree == skill[tmp]:
                tmp += 1
            if tmp == len(skill):
                break
        if tmp == check:
            answer += 1
    return answer