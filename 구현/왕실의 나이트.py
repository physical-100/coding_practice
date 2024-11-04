input = input()
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(8):
  if input[0] == list[i]:
    y = i + 1
x = int(input[1])
#8X8 배열 상하좌우 8가지 경우의 수가 가능한지 본다
case = [1, -1]
count = 0
move = [[1, 2], [2, 1]]
for i in range(2):
  for j in range(2):
    nx = x + (move[i][0] * case[j])
    for k in range(2):
      ny = y + (move[i][1] * case[k])
      if 0 < nx < 9 and 0 < ny < 9:
        count += 1
print(count)
