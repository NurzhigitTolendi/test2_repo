# Tuples

ourtuple = ("Say My Name", "I Am The One Who Knocks", 2008, "Better Call Saul", "Welcome to Los Pollos Hermanos family")

print(ourtuple)

Heisenberg, Walter, year, Saul, Gus = ourtuple

print(Walter)
print(Heisenberg)
print(year)
print(Saul)
print(Gus)

# tuple slicing
numbers = (0, 1, 2, 3, 4, 5)
print(numbers[1:4])  # Вывод: (1, 2, 3)
print(numbers[:3])   # Вывод: (0, 1, 2)
print(numbers[::2])  # Вывод: (0, 2, 4) (каждый второй элемент)


# tuples are immutable 
my_tuple = (1, 2, 3)
my_tuple[0] = 100  # Error: 'tuple' object does not support item assignment

#tuples faster than lists