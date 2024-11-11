import math
N = int(input())
case = []
for _ in range(N):
    case.append(list(map(int, input().split())))
for test_case in case:
    x1, y1, r1, x2, y2, r2 = test_case
    d = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
    # 교점 개수 계산
    if d > r1 + r2:
        count = 0  # 두 원이 멀리 떨어져 있음
    elif d < abs(r1 - r2):
        count = 0  # 한 원이 다른 원 안에 있음
    elif d == 0 and r1 == r2:
        count = -1  # 두 원이 동일함 (무한대의 교점)
    elif d == r1 + r2 or d == abs(r1 - r2):
        count =1 # 한 점에서 만남 (외접 또는 내접)
    else:
        count =2  # 두 점에서 만남
    print(count)

