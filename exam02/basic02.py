# 파일 입출력

f = open("/Users/limjun-young/workspace/privacy/dev/test/test.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

f = open("/Users/limjun-young/workspace/privacy/dev/test/test.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("/Users/limjun-young/workspace/privacy/dev/test/test.txt", 'r')
for line in f:
    line = line.strip()
    print(line)
f.close()

f = open("/Users/limjun-young/workspace/privacy/dev/test/test.txt", 'a')
for i in range(5, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()
