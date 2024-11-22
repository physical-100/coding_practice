#그룹의 개수를 찾고 적은 개수를 반환.
str = input()
count_0 = 0
count_1 = 0
for i in range(len(str)):
    if i == 0 :
        if str[i] =='0':
            count_0 += 1
        else:
            count_1 += 1
    else:
        if str[i]!=str[i-1]:
            if str[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
print(min(count_0,count_1))