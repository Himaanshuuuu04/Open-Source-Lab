filename = "sample_lines.txt"

with open(filename, 'w') as file:
    file.write("First line\nSecond line\nThird line\nFourth line\nFifth line")

print(f"Original content of {filename}:")
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

print(f"\nLines in reverse order:")
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())
