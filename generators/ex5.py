def count(n):
    while n >= 0:
        yield n
        n -= 1
n_value = 5
for number in count(n_value):
    print(number)
