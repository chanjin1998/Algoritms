import sys
n = int(sys.stdin.readline())
emoticon = set()
cnt = 0
for _ in range(n):
    word = input()

    if word != 'ENTER':
        if word not in emoticon:
            cnt += 1
            emoticon.add(word)
    # ENTER이면, 기존에 접속한 회원 정보 초기화
    elif word == 'ENTER':
        emoticon.clear()
print(cnt)