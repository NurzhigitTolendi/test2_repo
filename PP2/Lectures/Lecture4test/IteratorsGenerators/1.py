class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Использование
it = MyIterator(0, 5)
for num in it:
    print(num)  # Выведет 0 1 2 3 4
