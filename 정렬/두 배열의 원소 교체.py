N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b, reverse=True)
for i in range(K):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break
print(sum(a))
