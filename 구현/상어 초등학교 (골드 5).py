import heapq

n = int(input())
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
cls = [[0] * (n + 1) for _ in range(n + 1)]  # 독립적인 2차원 리스트 생성
order = []
favorite = [[] for _ in range(n**2 + 1)]  # 학생 번호에 따른 좋아하는 친구 정보

# 입력 처리
for _ in range(n**2):
    a, b, c, d, e = map(int, input().split())
    order.append(a)
    favorite[a] = [b, c, d, e]

def check_friend(cls, stu, student):
    count = 0
    r, c = stu
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 1 <= nr <= n and 1 <= nc <= n and cls[nr][nc] in favorite[student]:
            count += 1
    return count

def check_zero(cls, student):
    count = 0
    r, c = student
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 1 <= nr <= n and 1 <= nc <= n and cls[nr][nc] == 0:
            count += 1
    return count

def set_friend(student, cls):
    q = []
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if cls[r][c] == 0:
                heapq.heappush(q, (-check_friend(cls, (r, c), student), -check_zero(cls, (r, c)), r, c))
    chosen_seat = heapq.heappop(q)
    cls[chosen_seat[2]][chosen_seat[3]] = student  # 학생 자리 배치
    return [chosen_seat[2], chosen_seat[3]]  # 리스트로 반환

# 자리 배치
# seat = [None] * (n**2 + 1)  # 학생 번호에 따라 자리 좌표를 저장
seat = [[] for _ in range(n**2 + 1)]
for stu in order:
    seat[stu] = set_friend(stu, cls)  # [r, c] 형식으로 저장

# 만족도 계산
satisfy = 0
for student in order:
    r, c = seat[student]  # [r, c] 형식으로 언패킹
    score = check_friend(cls, (r, c), student)
    if score == 1:
        satisfy += 1
    elif score == 2:
        satisfy += 10
    elif score == 3:
        satisfy += 100
    elif score == 4:
        satisfy += 1000

print(satisfy)
