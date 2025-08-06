numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1, 9, 4, 10]

print("Original list:")
print(numbers)

print("\nDuplicate elements:")
seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

for duplicate in duplicates:
    print(duplicate)

print("\nDuplicate elements with their count:")
count_dict = {}
for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1

for num, count in count_dict.items():
    if count > 1:
        print(f"{num}: appears {count} times")
