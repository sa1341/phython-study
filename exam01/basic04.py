# 딕셔너리 자료형

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(dic)
print(dic['name'])

dic['age'] = 32
print(dic)

del dic['age']
print(dic)

# 키 리스트 만들기
keys = dic.keys()
print(keys)

for k in dic.keys():
    print(k)

list = list(dic.keys())
print(list)

# value 리스트
values = dic.values()
print(values)

# key, value 쌍 얻기
print(dic.items())

# key, value 지우기
dic.clear()
print(dic)

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.get('name'))

print('name' in a)
print('email' in a)