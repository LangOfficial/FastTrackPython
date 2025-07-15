# 15-3. Sum of Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# list comprehension method 
total = sum([sum(row) for row in matrix])
# OR
# sum(sum(row) for row in matrix) (best method in terms of speed and mmeory)
# Instead of list comp, we use a generator object. 
# A generator is a special type of iterable that is more memory efficent than lists. This is not covered in the course.

# increment method
total = 0
total += sum(matrix[0])
total += sum(matrix[1])
total += sum(matrix[2])

# increment method #2 (2nd best method in terms of speed and memory efficiency. It is more flexible than generator comprehension since it can include more complex logic with conditionals and more.)
total = 0
for row in matrix:
    total += sum(row)

# addition method
total = sum(matrix[0]) + sum(matrix[1]) + sum(matrix[2])

print(total)
