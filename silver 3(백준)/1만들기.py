'''모든 경우의 수 구하기'''
# #1이 되는 최소값을 찾는다.
# N = int(input())
# count =0
# def check(N,m):
#   global count
#   if N==1:
#     count = min(count,m) if count!=0 else m
#   if N%3 ==0:
#     check(N//3,m+1)
#   if N%2 ==0:
#     check(N//2,m+1)
#   if N-1 >= 3:
#     check(N-1,m+1)
# check(N,count)
# print(count)
''' 메모리제이션  '''
# N = int(input())
# memo = {}

# def check(N):
#     if N == 1:
#         return 0
#     if N in memo:
#         return memo[N]
#     # 가능한 연산 중 최소 값을 선택
#     result = check(N - 1) + 1
#     if N % 2 == 0:
#         result = min(result, check(N // 2) + 1)
#     if N % 3 == 0:
#         result = min(result, check(N // 3) + 1)

#     memo[N] = result
#     return result

# print(check(N))
'''동적 할당법'''
N = int(input())

# DP 테이블 생성: 각 인덱스는 해당 숫자까지의 최소 연산 횟수를 저장
dp = [0] * (N + 1)
#2부터 역으로 올라가면서 2나 3으로 나눠지는값은 해당 dp값에 1을 더하여 저장
for i in range(2, N + 1):
    # 기본적으로 1을 빼는 연산을 고려
    dp[i] = dp[i - 1] + 1
    # 2로 나누어 떨어지면 2로 나누는 연산과 비교하여 최소값 저장
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나누어 떨어지면 3으로 나누는 연산과 비교하여 최소값 저장
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[N])
