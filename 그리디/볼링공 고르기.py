n , m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
result = [0]*(m+1)
case = 0
for i in a :
        result[i]+=1
#개수 파악
for i in range(1,m):
    for j in range(i+1,m+1):
        case += result[i]*result[j]
print(case)

# 코드 최적화를 해보자.