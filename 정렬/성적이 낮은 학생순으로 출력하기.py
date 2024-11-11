N = int(input())
info = []
for _ in range(N):
  a,b = input().split()
  info.append((a,int(b)))
def score(data):
  return data[1]

info = sorted(info,key=lambda student: student[1])
#표현식 알아두기
s = []
for student in info:
  s.append(student[0])
print (s)