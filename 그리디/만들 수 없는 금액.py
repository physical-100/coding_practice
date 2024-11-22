#만들수 없는 양의  정수 금액의 최솟값을 뽑아라
# from itertools import combinations
# n = int(input())
# a = list(map(int, input().split()))
# available = set()
# for i in range(len(a)):
#     b= list(combinations(a,i))
#     for c in b:
#         available.add(sum(c))
# for i in range(max(available)):
#     if i not in available:
#         print(i)
#         break
#시간 복잡도가 너무 크다
n = int(input())
a = list(map(int, input().split()))
a.sort()
target = 1
for i in a :
    if i > target :
        break
    target+= i

print(target)
'''
왜 어렵냐..
'''