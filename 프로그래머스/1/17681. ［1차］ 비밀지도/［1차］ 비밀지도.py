def solution(n, arr1, arr2):
    result = []
    graph1 = []
    graph2 = []
    for i in range(n):
        tmp1 = bin(arr1[i])
        tmp2 = bin(arr2[i])
        if len(tmp1[2:]) < n:
            alpha = "0" * (n-len(tmp1[2:])) + tmp1[2:]
            graph1.append(alpha)
        else:
            graph1.append(tmp1[2:])
        if len(tmp2[2:]) < n:
            alpha = "0" * (n-len(tmp2[2:])) + tmp2[2:]
            graph2.append(alpha)
        else:
            graph2.append(tmp2[2:])
    print(graph1)
    print(graph2)
    for i in range(n):
        answer = ""
        for j in range(n):
            if graph1[i][j] == '1' or graph2[i][j] == '1':
                answer += '#'
            else:
                answer += " "
        result.append(answer)
    return result