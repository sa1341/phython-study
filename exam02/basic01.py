def add(a, b):
    result = a + b
    return result


sum = add(a=3, b=4)
print(sum)


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

sum = add_many(1, 3, 5, 7)
print(sum)
