numbers = range(1, 101)
numbers = list(numbers)

even = [x for x in numbers if x % 2 == 0]

print sum(even)