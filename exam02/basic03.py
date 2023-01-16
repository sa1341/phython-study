# 테스트를 위한 Faker 라이브러리 예제코드
from faker import Faker
fake = Faker()
print(fake.name())

test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)