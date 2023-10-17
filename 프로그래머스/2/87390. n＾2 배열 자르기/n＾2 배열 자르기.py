def solution(n, left, right):
    answer = []
    graph = []
    for i in range(left,right+1):
        graph.append(max(i//n,i%n)+1)
   
    return graph
    # return graph