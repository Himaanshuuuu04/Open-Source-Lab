numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Original list:")
print(numbers)

print("\nEven numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print("\nEven numbers using list comprehension:")
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
