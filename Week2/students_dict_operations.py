students = {
    "Alice": 18,
    "Bob": 22,
    "Charlie": 19,
    "Diana": 25,
    "Emma": 21
}

print("Original dictionary:")
print(students)

print("\na. Students whose age is greater than 20:")
for name, age in students.items():
    if age > 20:
        print(f"{name}: {age}")

print("\nb. Adding new student with age 30:")
students["Frank"] = 30
print(f"After adding Frank: {students}")

print("\nc. All students using .items():")
for name, age in students.items():
    print(f"{name}: {age}")

print("\nd. Deleting a student:")
print(f"Before deletion: {students}")
del students["Charlie"]
print(f"After deleting Charlie: {students}")

print("\ne. Average age of all students:")
total_age = sum(students.values())
average_age = total_age / len(students)
print(f"Total students: {len(students)}")
print(f"Total age: {total_age}")
print(f"Average age: {average_age:.2f}")
