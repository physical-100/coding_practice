# N = int(input())
# move = input().split() # 문자열의 경우 그냥 받으면 된다.
# position = [1, 1]
# for i in range(len(move)):
#   x, y = position
#   new_x =x
#   new_y =y
#   if move[i] == 'R':
#     new_y = new_y+1
#   elif move[i] == 'L':
#     new_y= new_y-1 
#   elif move[i] == 'U':
#     new_x = new_x-1
#   else :
#     new_x = new_x+1
#   if new_x < 1 or new_x > N or new_y < 1 or new_y > N:
#     continue
#   else:
#     position = [new_x, new_y]
# print(position[0], position[1])

n = int(input())
x, y = 1, 1
plans = input().split()
# Lz R, uZ。에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types =['L', 'R', 'U','D']
# 이동 계획을 하나씩 확인
for plan in plans:
# 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx,ny
print(x,y)