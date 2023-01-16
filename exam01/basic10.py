a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)


# range 함수
a = range(1, 11)
print(a)

add = 0
for i in range(1, 11):
    add = add + i

print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


# 구구단 print 함수는 default로 \n 개행문자가 셋팅되어 있음.
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print('')

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

# 짝수만 배열에 담기
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
