# N = int(input())
# paper = []
# result = {-1:0, 0:0,1:0}
# def divide (x,y,N):
#     curr = paper[x][y]
#     for i in range(x,x+N):
#         for j in range(y,y+N):
#             if paper[i][j] != curr :
#                 next = N//3
#                 divide(x, y, next)  # 1번째 block (0,0)
#                 divide(x, y + next, next)  # 2번째 block (0,1)
#                 divide(x, y + (next * 2), next)  # 3번째 block (0,2)
#                 divide(x + next, y, next)  # 4번째 block (1,0)
#                 divide(x + next, y + next, next)  # 5번째 block (1,1)
#                 divide(x + next, y + (next * 2), next)  # 6번째 block (1,2)
#                 divide(x + (next * 2), y, next)  # 7번째 block (1,0)
#                 divide(x + (next * 2), y + next, next)  # 8번째 block (1,1)
#                 divide(x + (next * 2), y + (next * 2), next)  # 9번째 block (1,2)
#                 return
#     result[curr]+=1
#     return
#
# for i in range(N):
#     a = list(map(int, input().split()))
#     paper.append(a)
# divide(0,0,N)
# for i in result.values():
#     print(i)
#

n = int(input())
paper = []
result = {-1:0, 0:0, 1:0 }
for _ in range(n):
    paper.append(list(map(int,input().split())))

def divide(row, col, n):
    #현재 확인하는 값을 고른다.
    curr = paper[row][col]
    for i in range(row,row+n):
        for j in range(col,col+n):
            if paper[i][j]!= curr:
                next = n//3
                divide(row,col,next)
                divide(row+next,col,next)
                divide(row+(next*2),col,next)
                divide(row, col+ next, next)
                divide(row + next, col+ next, next)
                divide(row + (next * 2), col+ next, next)
                divide(row, col+ (next * 2), next)
                divide(row + next, col+ (next * 2), next)
                divide(row + (next * 2), col+ (next * 2), next)
                return
    result[curr]+=1
    return
divide(0,0,n)
for i in result.values():
    print(i)
