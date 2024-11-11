N = int(input())
coin_type = [500, 100, 50, 10]
count = 0
for coin in coin_type:
  count += N // coin
  N %= coin
print("최소 동전 개수", count)
