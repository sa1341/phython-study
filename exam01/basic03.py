# 리스트 자료형
a = [1, 2, 3]
print(a[-1])

a = [1, 2, 3]
b = [4, 5, 6]
print(a +  b)

# 리스트 반복하기
print(a * 3)

# 리스트 길이구하기
print(len(a))

# 리스트 값 삭제
del a[1]
print(a)

del a[0:]
print(a)

a.append(1)
print(a)

a.append([1, 2, 3])
print(a)

# 숫자 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)

# 알파벳 정렬
a = ['a', 'c', 'b']
a.sort()
print(a)

# 리스트 뒤집기
a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))

# 리스트에 요소 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)

# 리스트에 요소 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a.remove(3)
print(a)

a.pop()
print(a)
print(a.count(2))

# 리스트 확장
a = [1,2,3]
a.extend([4, 5])
print(a)