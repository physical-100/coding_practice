N = int(input())
count = 0
for i in range(0, N + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1
print(count)
#str로 변환해서 비교하는거까진 좋았는데 아직 한참멀었다...
