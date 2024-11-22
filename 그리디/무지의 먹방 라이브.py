import heapq

def solution(food_times, k):
    # 전체 음식 시간이 k보다 작거나 같으면 -1 반환
    if sum(food_times) <= k:
        return -1

    # (음식 시간, 인덱스)로 힙 생성
    heap = [(time, i) for i, time in enumerate(food_times)]
    heapq.heapify(heap)  # 최소 힙으로 변환

    prev_time = 0  # 이전 라운드의 음식 시간
    total_foods = len(food_times)  # 남은 음식 개수

    while heap:
        # 현재 가장 적은 음식 시간
        time = heap[0][0] - prev_time
        # 현재 라운드에서 제거할 총 시간
        deltime = time * total_foods

        if deltime > k:  # 남은 k를 초과하면 멈춤
            k %= total_foods
            remaining = sorted(heap, key=lambda x: x[1])  # 인덱스 기준 정렬
            return remaining[k][1] + 1  # 1-based index 반환

        # k에서 현재 라운드 시간 제거
        k -= deltime
        prev_time = heapq.heappop(heap)[0]  # 가장 적은 음식 제거
        total_foods -= 1  # 음식 개수 감소

    return -1
