import itertools
def solution(word):
    
    # 모음 리스트
    vowels = ['A', 'E', 'I', 'O', 'U']

    # 결과를 저장할 리스트
    result = []

    # 1개에서 4개까지의 문자열 생성
    for length in range(1, 6):  # 1부터 4까지
        combinations = itertools.product(vowels, repeat=length)
        for combination in combinations:
            result.append(''.join(combination))

    # 결과 출력
    result.sort()

    answer = 0
    answer = result.index(word) + 1
    return answer
