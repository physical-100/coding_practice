N, K = map(int, input().split())
#목이 k보다 작아진 경우 -1씩하는건 연산 시간이 늘어날 수 있다.
count = 0
while N != 1:
  if N % K == 0:
    N //= K
  elif N < K:
    count += N - 1
    break
  else:
    N -= 1
  count += 1
print(count)
