if 4 in [1, 2, 3, 4]: print("4가 있습니다.")

# 조건문
a = 3
if a > 1:
    print('a는 1보다 큽니다.')
    print('조건이 성립')

print('조건문 종료')

# 반복문 for
print("반복문 for 시작")
for a in [1, 2, 3]:
    print(a)

# 반복문 while
print("반복문 while 시작")
i = 0
while i < 3:
    i = i + 1
    print(i)


# 함수
print("함수 호출")
def add(a, b):
    return a + b

print(add(3, 4))