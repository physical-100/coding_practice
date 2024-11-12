N = int(input())
count = [0]*1001
count[1] = 1
count[2] = 3
for i in range(3,N+1):
    count[i] = (count[i-1]+ count[i-2]*2)% 796796
print(count[N])