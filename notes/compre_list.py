# List comprehension = A consice way to create lists, compact and easy to read.
# [expression for value ininterable if condition]

#List comprehension
numbers = [num * 2 for num in range(1, 11)]


# Normal way
# for num in range(1, 11):
#     numbers.append(num * 2)

print(numbers)

