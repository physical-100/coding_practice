def dfs(x, y):  #상하좌우 4방향의 0을 찾아서 다 1로 바꾸고 반환
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  else:
    if graph[x][y] == 0:
      graph[x][y] = 1
      dfs(x - 1, y)
      dfs(x, y - 1)
      dfs(x + 1, y)
      dfs(x, y + 1)
      return True
    return False


N, M = map(int, input().split())
graph = []
for i in range(N):  #띄워쓰기 안된 숫자는 그냥 이렇게 넣으면 된다.
  graph.append(list(map(int, input())))
count = 0
dx = [1, -1, 0, 0]  # 상하좌우 확인
dy = [0, 0, 1, -1]  #
for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      count += 1
print(count)
