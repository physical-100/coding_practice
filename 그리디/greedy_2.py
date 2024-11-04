N, M, K = map(int, input().split())
number = list(map(int, input().split()))
sum = 0
number.sort()
k = K
for _ in range(M):
  if k > 0:
    sum += number[-1]
    k -= 1
  elif k == 0:
    sum += number[-2]
    k = K
print(sum)
