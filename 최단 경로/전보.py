#도시의 개수 N. 통로의 개수 M. 메시지를 보내고자 하는 도시 C
import heapq
N,M,C = map(int,input().split())
distance = [1e9]*(N+1)
distance[C] = 0
graph = [[] for _ in range(N+1)]
for _ in range(M):
    X,Y,Z = map(int,input().split())
    graph[X].append((Y,Z))
def dijkstra(start):
    q = []
    heapq.heappush(q,(distance[start],start))
    while q:
        dist,node = heapq.heappop(q)
        if distance[node]< dist:
            #한번 방문했던 노드이다.
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost< distance[i[0]]:
                distance[i[0]]  = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(C)
get_message = []
for i in range(1,N+1):
    if distance[i]!=0 and distance[i]!=1e9:
        get_message.append(distance[i])
print(len(get_message),max(get_message))





