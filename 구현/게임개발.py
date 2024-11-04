N,M  = map(int,input().split())
s_x,s_y,dir = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
checked = [[False]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy= [0, 1,0,-1]
count = 1
turn_time = 0
checked[s_x][s_y] = True # 현재 좌표 방문 처리
while True:
  dir = dir-1 if dir> 0 else 3 #왼쪽 방향으로 이동
  n_x= s_x+ dx[dir]
  n_y = s_y + dy[dir]
  if map[n_x][n_y]==0 and checked[n_x][n_y]==False and -1<n_x<M and -1<n_y<N:
    s_x = n_x
    s_y = n_y
    checked[s_x][s_y] = True
    count +=1
    turn_time = 0
    continue
  else: 
    turn_time +=1
  if turn_time == 4:
    n_x= s_x- dx[dir]
    n_y = s_y -dy[dir]
    if map[n_x][n_y]==0 :
      s_x = n_x
      s_y = n_y
    else:
      break
    turn_time = 0
print(count)
