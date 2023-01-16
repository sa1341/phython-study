# 객체 메모리 주소값 출력
a = [1, 2, 3]
print(id(a))

b = a
print(a is b)

a[1] = 4
print(a)
print(b)

from copy import copy
a = [1, 2, 3]
b = copy(a)
print(b)
print(a is b)

(a, b) = ('python', 'life')
print("a: " + a + ", b:" + b)

[a,b] = ['kotlin', 'java']
print("a: " + a + ", b:" + b)

# swap
a = 3
b = 5
print("a: " + str(a) + ", b:" + str(b))
a, b = b, a
print("a: " + str(a) + ", b:" + str(b))
