N,M = map(int,input().split())
a= []
for i in range(N):
    a.append(int(input()))
dp = [10001]* (M+1)
dp[0] = 0
#가장 큰 값으로 채워 넣음
#이후 배열에 있는 값들 하나씩 점화식 사용
for i in range(N):
    for j in range(a[i],M+1):
        if dp[j-a[i]]!= 10001:
            dp[j] = min(dp[j],dp[j-a[i]]+1)
if dp[M]!= 10001:
    print(dp[M])
else:
    print(-1)
