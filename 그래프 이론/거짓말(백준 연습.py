# def find_parent(parent,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]
# # def union_parent(parent,list):
# #     min_val = 1e5
# #     for i in range(len(list)):
# #         min_val = min(min_val,find_parent(parent,list[i]))
# #     for i in range(len(list)):
# #         parent[list[i]] = min_val
#
# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b] =a
#     else:
#         parent[a] =b
#
# N , M = map(int, input().split())
# parent = [0]*(N+1)
# for i in range(1,N+1):
#     parent[i] = i
# #부모노드 초기화
# truth = list(map(int, input().split()))
# party =[]
# for _ in range(M):
#     party.append(list(map(int, input().split())))
#
#
# if truth[0] == 0:
#     print(M)
# else:
#     truth = truth[1:]
#     for p in party:
#         if len(p)>=3:
#             # union_parent(parent,p[1:])
#             for i in range(1,len(p)-1):
#                 union_parent(parent,p[i],p[i+1])
#             #모든 파티에 대해서 합집합 진행
#         else:
#             continue
#
#     #이후 진실을 아는 사람들의 parent가 포함되지 않은 경우의 수만 출력
#     tru_parent = []
#     count = 0
#     for t in truth:
#         tru_parent.append(parent[t])
#     for p  in party:
#         all_check=0
#         for i in range(1,len(p)):
#             if parent[p[i]] not in tru_parent:
#                 all_check+=1
#         if all_check== len(p)-1:
#             count+=1
#     print(count)
#     print(parent)
#
def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


# 사실을 아는 사람과 Union시, 해당 사람이 부모노드가 되도록
def union(parent, a, b, know_truth):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a in know_truth and b in know_truth:
        return

    if a in know_truth:
        parent[b] = a

    elif b in know_truth:
        parent[a] = b

    else:# 사실을 아는 사람과 union이 아닐때는 일반 Union
        if a < b:
            parent[b] = a

        else:
            parent[a] = b


n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(n + 1)) # list 초기화

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        union(parent, party[i], party[i + 1], know_truth)
    parties.append(party)

ans = 0
for party in parties:
    for i in range(len(party)):
        if find_parent(parent, party[i]) in know_truth:
            break

    else:
        ans += 1

print(ans)
