import copy
def merge_right(p):
    merged = []
    i = len(p) - 1
    
    while i >= 0: 
        if i > 0 and p[i] == p[i - 1]:
            merged.append(p[i] * 2)
            i -= 2
        else:
            merged.append(p[i])
            i -= 1
    
    merged.reverse()
    return merged

def merge_left(p):
    merged = []
    i = 0
    
    while i < len(p):  
        if i < len(p) - 1 and p[i] == p[i + 1]:
            merged.append(p[i] * 2)
            i += 2
        else:
            merged.append(p[i])
            i += 1
    
    return merged

def shift_right(matrix):
    for row in matrix:
        non_zero_elements = [num for num in row if num != 0]
        a = merge_right(non_zero_elements)
        new_row = [0] * (len(row) - len(a)) + a
        for i in range(len(row)):
            row[i] = new_row[i]
    return matrix

def shift_left(matrix):
    for row in matrix:
        non_zero_elements = [num for num in row if num != 0]
        b = merge_left(non_zero_elements)
        new_row = b + [0] * (len(row) - len(b))
        for i in range(len(row)):
            row[i] = new_row[i]
    return matrix

def shift_up(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for col in range(cols):
        non_zero_elements = [matrix[row][col] for row in range(rows) if matrix[row][col] != 0]
        b = merge_left(non_zero_elements)
        new_column = b + [0] * (rows - len(b))
        
        for row in range(rows):
            matrix[row][col] = new_column[row]
    return matrix

def shift_down(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for col in range(cols):
        non_zero_elements = [matrix[row][col] for row in range(rows) if matrix[row][col] != 0]
        a = merge_right(non_zero_elements)
        new_column = [0] * (rows - len(a)) + a
        
        for row in range(rows):
            matrix[row][col] = new_column[row]
    return matrix

def move(n, matrix):
    global ans
    if n == 5:
        for i in range(N):
            for j in range(N):
                if matrix[i][j] > ans:
                    ans = matrix[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(matrix)
        if i == 0:
            move(n + 1, shift_left(copy_arr))
        elif i == 1:
            move(n + 1, shift_right(copy_arr))
        elif i == 2:
            move(n + 1, shift_up(copy_arr))
        else:
            move(n + 1, shift_down(copy_arr))
# 초기 설정
N = int(input())
block = [list(map(int, input().split())) for _ in range(N)]
ans = 0
n = 0
move(0,block)

print(ans)
