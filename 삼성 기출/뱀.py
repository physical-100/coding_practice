N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
dir_info = [(input().split()) for _ in range(L)]  # 초,방향 전환 정보
dx = [0, 1, 0, -1]  # 동,남,서,북
dy = [1, 0, -1, 0]
s = 0


def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


def turn_right():
  global direction
  direction += 1
  if direction == 4:
    direction = 0


direction = 0  #동쪽
x = 1
y = 1
snake_len = 1
snake = [[x, y]]
a, b = dir_info.pop(0)
while True:
  s += 1
  x = x + dx[direction]
  y = y + dy[direction]
  if x < 1 or x > N or y < 1 or y > N:
    break
  else:
    if [x, y] in apple:
      snake_len += 1
      apple.remove([x, y])
    if [x, y] in snake:
      break
    else:
      snake.append([x, y])
      if len(snake) > snake_len:
        snake.pop(0)
  # print(f"초:{s} 뱀 위치 : {snake}")
  if s == int(a):
    if b == 'L':
      turn_left()
    else:
      turn_right()
    if len(dir_info) != 1:
      a, b = dir_info.pop(0)
    else:
      a, b = dir_info[0]
print(s)
