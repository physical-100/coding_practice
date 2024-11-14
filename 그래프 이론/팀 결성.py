# n은 가능한 숫자 m은 입력으로 주어자는 연산의 개수
#0은 합치기 연산 1은 같은 팀 확인 연산
def find_parents(parents,x):
    if parents[x] != x:
        parents[x] = find_parents(parents,parents[x])
    return parents[x]
def union_parents(parents,a,b):
    a = find_parents(parents,a)
    b = find_parents(parents,b)
    if a<b:
        parents[b] =a
    else:
        parents[a] =b

n, m = map(int, input().split())
operations = []
for _ in range(m):
    a,b,c = map(int, input().split())
    operations.append((a,b,c))
parents = []
for i in range(n+1):
    parents.append(i)
for op in operations:
    x,y,z = op
    if x ==0:
        union_parents(parents,y,z)
    elif x == 1:
        if find_parents(parents,y)!= find_parents(parents,z):
            print("NO")
        else:
            print("YES")