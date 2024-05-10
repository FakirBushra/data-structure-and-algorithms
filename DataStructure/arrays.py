# Arrays
# Random Indexing

numbers = [11, 12, 13, 14, 15]
# print(numbers[0])

# numbers[0] = 7
# numbers[2] = "name"

# print(numbers)

# for num in numbers:
#    print(num)

# for i in range(len(numbers)):
#    print(numbers[i])

# print(numbers[1:3])
# print(numbers[:])
# print([numbers[:-3]])

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)
