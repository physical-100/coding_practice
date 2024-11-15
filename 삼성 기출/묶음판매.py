T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    #N%x가 x/2이상이면 묶음 세트  X개를 더 구매함
    if a<=(b/2) or a==1:
        print("no")
    else:
        print("yes")