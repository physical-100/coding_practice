#길 개수 n, 간선 m
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,x,y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)
    if x> y:
        parent[x] = y
    else:
        parent[y] = x

n, m = map(int, input().split())
graph  = []
parent = [0] * (n+1)
line  = [] #신장트리를 만족하는 간선을 담는 공간
#parent 초기화
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a, b , c = map(int, input().split())
    graph.append((c,a,b))
graph.sort()
#그래프  비용 순으로 정렬
for check in graph:
    c,b,a = check
    #사이클이 안 생길 때만 합집합 연산하고 비용을 추가함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,b,a)
        line.append(c)
# 반복문 과정에서 일일이 더한뒤 마지막에 변수에 저장된 값을 빼주는 것고 시간 연산을 줄이는 방법
print(sum(line[:-1]))
