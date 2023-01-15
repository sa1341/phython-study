# 숫자 연산
downloadRate = 800
downloadTime = 110

fileSize = (downloadRate * downloadTime) / 1000
print("file size: " + str(fileSize) + "MB")

# 배열 반복문
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")


# 문자열
food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he says.'
print(say)

multiline="""
Life is too short
You need python
"""
print(multiline)

# 문자열 곱하기
a = "python"
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))
# 인덱싱
print(a[3])
print(a[-2])

# 슬라이싱
a = "Life is too short, You need Python"
print(a[0:4])
print(a[19:])
print(a[:17])
print(a[19:-7])


# 문자열 포매팅
foramt = "I eat %d apples." % 3
print(foramt)

foramt = "I eat %s apples." % "five"
print(foramt)

number = 10
day = "three"
format = "I ate %d apples. so I was sick for %s days." % (number, day)
print(format)

# %s는 자동으로 % 뒤에 있는 값을 문자여롤 변경하기 때문에 타입은 중요하지않음.
format2 = "I have %s apples" % 3
print(format2)

format3 = "Error is %d%%." % 98
print(format3)

# 소수점 표현
f = "%0.4f" % 3.42134234
print(f)

# format 함수를 사용한 포매팅
format4 = "I eat {0} apples".format(3)
print(format4)

format4 = "I eat {0} apples".format("five")
print(format4)

number = 3
format4 = "I eat {0} apples".format(number)
print(format4)

format4 = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(format4)

name = '홍길동'
age = 30
format5 = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(format5)

# 문자열 관련 함수모음
a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('i'))
print(a.index('c')) # find와 다르게 해당 문자의 인덱스가 없으면 에러 발생!

# 문자열 삽입
str = ",".join("abcd")
print(str)
print(str.upper())
print(str.lower())

a = " hi "
print(a.lstrip()) # 왼쪽 공백 지우기
print(a.rstrip()) # 오른쪽 공백 지우기
print(a.strip()) # 양쪽 공백 지우기

# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기
a = "Life is too short"
print(a.split())