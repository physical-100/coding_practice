from collections import deque
import copy
#값을 복제하기 위해
N = int(input())
#차수
indegree = [0]*(N+1)
# 강의 시간
time =[0]*(N+1)
graph = [[]for _ in range(N+1)]
for i in range(1,N+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] +=1
        #선수과목이 j이고 이후 과목이 i이기 때문에
        graph[j].append(i)

def torpologicalSort():
    result = copy.deepcopy(time)
    # 결과값은 변형이 필요하기 때문에 copy 라이브러리 사용
    q = deque() # 큐 선언
    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        x = q.popleft()
        for i in graph[x]:
            #x를 선행되어야하는 과목 i 의 소요 시간을 바꾼다
            result[i] = max(result[i],result[x]+time[i])
            #차수를 낮춰서 0이되면 큐에 넣음
            indegree[i]-=1
            if indegree[i] ==0:
                q.append(i)
    for i in range(1,N+1):
        print(result[i])

torpologicalSort()