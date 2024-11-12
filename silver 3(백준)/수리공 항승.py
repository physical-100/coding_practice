N,tape_len = map(int,input().split())
hole_position = list(map(int,input().split()))
hole_position.sort()
#중복을 없앤다
count = 0
possible = 0
for i in hole_position:
    if i >= possible:
        possible  = i + tape_len
        count+=1
print(count)