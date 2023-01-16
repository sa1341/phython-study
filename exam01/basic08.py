money = True

if money:
    print("택시를 타고 간다")
else:
    print("버스를 타고 간다.")

# if문 논리 연산

money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타고 간다.")
else:
    print("걸어간다.")


print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' not in ('a', 'b', 'c'))

# 다중 조건
pocket = ['paper', 'handphone']
card = True

if 'money' in pocket:
    print("택시를 타고간다.")
elif card:
    print("택시를 타고간다.")
else:
    print("걸어간다.")

if 'money' in pocket: pass
else: print("카드를 꺼낸다.")