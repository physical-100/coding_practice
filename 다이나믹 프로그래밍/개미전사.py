N =int(input())
store = list(map(int,input().split()))
dp = [0]*101
dp[1] = store[0]
dp[2] = max(store[0],store[1])
for i in range(3,N+1):
    dp[i] = max(dp[i-1], dp[i-2]+store[i-1])
print(dp[N])