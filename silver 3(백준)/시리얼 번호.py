import re
# 문자열에서 숫자의 합을 구하는 함수
def sum_of_digits(s):
    digits = re.findall(r'\d', s)
    return sum(int(d) for d in digits)

N = int(input())
guitar = []
for _ in range(N):
    guitar.append(input())

# 길이, 숫자 합, 사전순으로 정렬
guitar = sorted(guitar, key=lambda x: (len(x), sum_of_digits(x), x))

for i in guitar:
    print(i)


'''
이게 맞나..
'''