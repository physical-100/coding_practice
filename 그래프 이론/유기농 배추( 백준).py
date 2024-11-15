from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs
def bfs(a, b):
    q = deque()
    q.append((a, b))
    array[a][b] = 0  # 방문처리

    while q:
        x, y = q.popleft()

        for i in range(4):  # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:  # 좌표 확인
                continue
            if array[nx][ny] == 1:  # 배추가 심어져 있으면
                q.append((nx, ny))
                array[nx][ny] = 0


for i in range(T):  # T번 반복
    M, N, K = map(int, input().split())
    array = [[0] * N for i in range(M)]

    for j in range(K):
        x, y = map(int, input().split())
        array[x][y] = 1
    # print(array)

    # 그래프를 순회하며 탐색
    total = 0
    for i in range(M):
        for j in range(N):
            if array[i][j] == 1:  # 배추가 심어져 있으면 bfs 수행
                bfs(i, j)
                total += 1
    print(total)