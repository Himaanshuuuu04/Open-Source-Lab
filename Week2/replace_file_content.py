filename = "sample.txt"

with open(filename, 'w') as file:
    file.write("This is some sample content in the file.")

print(f"Original content of {filename}:")
with open(filename, 'r') as file:
    original_content = file.read()
    print(original_content)

with open(filename, 'w') as file:
    file.write("Hi, I am currently pursuing my BTech from Jaypee.")

print(f"\nNew content of {filename}:")
with open(filename, 'r') as file:
    new_content = file.read()
    print(new_content)
