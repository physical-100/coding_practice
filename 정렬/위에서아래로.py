N = int(input())
a = []
for _ in range(N):
  a.append(int(input()))
b = sorted(a, reverse=True)
print(b)
