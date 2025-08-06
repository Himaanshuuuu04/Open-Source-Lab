# Tuple operations program

# Create a tuple of 5 students
students = ("Alice", "Bob", "Charlie", "Diana", "Emma")

# a. Display all students
print("a. All students:")
print(students)

# b. Add new student
print("\nb. Adding new student:")
new_students = students + ("Frank",)
print(f"After adding: {new_students}")

# c. Delete a student  
print("\nc. Deleting a student:")
# Convert to list, remove, convert back
temp_list = list(students)
temp_list.remove("Charlie")
after_deletion = tuple(temp_list)
print(f"After removing Charlie: {after_deletion}")

# d. Slicing from first to third index
print("\nd. Students from index 1 to 3:")
print(students[1:4])

# e. Try to modify second index
print("\ne. Can we modify index 2?")
try:
    students[2] = "Modified"
except TypeError:
    print("No! Tuples are immutable - cannot modify elements")
