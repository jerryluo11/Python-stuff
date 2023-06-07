#remove duplicates

numbers = [1,2,3,4,5,5,5,6,6]

for item in numbers:
    if numbers.count(item) != 1:
        numbers.remove(item)

print(numbers)