total, win = map(int, input().split())
prob = win * 100 // total  # 정수 연산으로 초기 확률 계산

# 확률이 99 이상이면 더 이상 올릴 수 없음
if total == win or prob >= 99:
    print(-1)
else:
    # 이진 탐색 초기값 설정
    start = 0
    end = 10 ** 9  # 가능한 최대 승리 수 추가 범위로 설정

    result = -1  # 결과 값 초기화
    while start <= end:
        count = (start + end) // 2
        # 새로 계산한 확률
        new_prob = (win + count) * 100 // (total + count)

        if new_prob > prob:  # 확률이 증가하는 최소 count 찾기
            result = count
            end = count - 1
        else:
            start = count + 1

    print(result)
