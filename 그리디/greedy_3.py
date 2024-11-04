N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
row_min = []
for row in matrix:
  row_min.append(min(row))
print(max(row_min))
# 이렇게 말고 입력 받을 때 바로 min을 구하는 더 간단한 방법도 있다.
