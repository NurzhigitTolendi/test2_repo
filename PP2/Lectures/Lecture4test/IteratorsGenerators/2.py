def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

for num in my_generator():
    print(num)



def count(start=0):
    while True:
        yield start
        start += 1

counter = count()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

print(next(counter))
print(next(counter))


