N  = int(input())
m  = list(map(int, input().split()))
m.sort()
count = 0
while len(m)!=0:
    x= m.pop(-1)
    for i in range(x-1):
        x = m.pop(-1)
    count+=1
print(count)