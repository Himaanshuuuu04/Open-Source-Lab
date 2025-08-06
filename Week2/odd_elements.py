numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Original list:")
print(numbers)

print("\nOdd elements using list comprehension:")
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
