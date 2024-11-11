N , M  = map (int, input().split())
ricecake = list(map(int, input().split()))
def binary_search(ricecake,M,low,high):
    result = 0
    if low > high:
        return None
    while low <= high:
        diff = 0
        h = (low + high) // 2
        for i in ricecake:
            if i>h:
                diff = diff +(i-h)
        if diff == M :
            return h
        elif diff < M:
            high = h - 1
            # 떡의 양이 충분한 경우 덜 자르기
        else :
            result = h  # 최대한 덜 잘랐을 때가 정답이므로
            low = h + 1
    return result

ricecake.sort()
result = binary_search(ricecake, M, 0, ricecake[-1])
print(result)