from collections import deque

def precompute_scores(Map):
    score_map = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if score_map[i][j] == 0:  # 아직 점수가 계산되지 않은 경우
                score_map[i][j] = find_score(Map[i][j], i, j)
    return score_map

def find_score(score, dx, dy):
    q = deque([(dx, dy)])
    visited = set([(dx, dy)])
    search = [(0,1),(0,-1),(1,0),(-1,0)]
    cnt = 0
    while q:
        sx, sy = q.popleft()
        cnt += 1
        for s in search:
            x,y = s
            nx, ny = sx + x, sy + y
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and Map[nx][ny] == score:
                visited.add((nx, ny))
                q.append((nx, ny))
    return cnt * score  # C * B

def rotate_clockwise(direction):
    x, y = direction
    return (y, -x) if x != 0 else (y, x)

def rotate_counter(direction):
    x, y = direction
    return (y, x) if y == 0 else (-y, x)

def change_direction(direction):
    x, y = direction
    return (-x, y) if y == 0 else (x, -y)

def roll_dice(dice, direction):
    x, y = direction
    top, bottom, north, south, west, east = dice
    if x == 0 and y == 1:  # 동쪽
        dice = [west, east, north, south, bottom, top]
    elif x == 0 and y == -1:  # 서쪽
        dice = [east, west, north, south, top, bottom]
    elif x == 1 and y == 0:  # 남쪽
        dice = [north, south, bottom, top, west, east]
    elif x ==-1 and y == 0:
        dice = [south, north, top, bottom, west, east]
    return dice

# 초기 입력
dice = [1, 6, 2, 5, 4, 3]
direction = (0, 1)
N, M, rep = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
# 각 칸의 점수 미리 계산
score_map = precompute_scores(Map)
# 주사위 이동 시작
s_x, s_y = 0, 0
score = 0
for i in range(rep):
    x, y = direction
    # 지도 밖으로 나갈 경우 방향 반대로
    if not (0 <= s_x + x < N and 0 <= s_y + y < M):
        direction= change_direction(direction)
        x,y = direction
    
    s_x += x
    s_y += y

    # 현재 위치에서 점수 획득
    score += score_map[s_x][s_y]
    # print(f"{i}번째 방향:{direction}" )
    # print(f"{i}번째 값:{score}" )
    # # 주사위 굴리기
    dice = roll_dice(dice, direction)
    A = dice[1]
    # print(f"{i}번째 주사위값:{A}" )
    B = Map[s_x][s_y]
    # print(f"{i}번째 지도값:{B}" )

    # 이동 방향 결정
    if A > B:
        direction = rotate_clockwise(direction)
    elif A < B:
        direction = rotate_counter(direction)

print(score)
