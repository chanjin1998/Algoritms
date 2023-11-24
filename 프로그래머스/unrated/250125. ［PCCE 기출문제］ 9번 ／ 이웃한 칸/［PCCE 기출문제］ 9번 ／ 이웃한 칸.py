from collections import deque
def solution(board, h, w):
    # answer = 0
    max_h = len(board)
    max_w = len(board[0])
    def bfs(h,w):
        answer = 0
        # q = deque()
        # q.append((h,w))
        dh = [0,1,-1,0]
        dw = [1,0,0,-1]
        
        # while q:
        #     h,w = q.popleft()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]

            if 0<=nh<max_h and 0<=nw<max_w:
                print(board[h][w],board[nh][nw])
                if board[h][w] == board[nh][nw]:
                    answer += 1
        return answer
    res = bfs(h,w)
    return res