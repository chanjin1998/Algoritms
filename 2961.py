def dfs(idx, s_mul, b_sum):
    global min_difference

    if idx == N:  # 모든 재료를 다 확인한 경우
        if s_mul != 1 and b_sum != 0:  # 물이 아닌 최소 1개의 재료를 사용했을 때
            difference = abs(s_mul - b_sum)
            min_difference = min(min_difference, difference)
        return

    # 재료를 선택하는 경우
    dfs(idx + 1, s_mul * ingredients[idx][0], b_sum + ingredients[idx][1])

    # 재료를 선택하지 않는 경우
    dfs(idx + 1, s_mul, b_sum)


if __name__ == "__main__":
    N = int(input())  # 재료의 개수

    # 재료의 신맛과 쓴맛을 입력받아 리스트에 저장
    ingredients = []
    for _ in range(N):
        s, b = map(int, input().split())
        ingredients.append((s, b))

    min_difference = float('inf')  # 신맛과 쓴맛의 차이를 저장할 변수, 초기값은 최대값으로 설정

    for i in range(N):
        # 모든 재료를 하나씩 선택하는 경우 탐색
        dfs(i, ingredients[i][0], ingredients[i][1])

    print(min_difference)  # 신맛과 쓴맛의 차이의 최소값 출력
