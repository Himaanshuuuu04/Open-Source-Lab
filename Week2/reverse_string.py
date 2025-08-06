text = "Hello World Python Programming"

print("Original string:")
print(text)

print("\nReversed string:")
print(text[::-1])

print("\nReversed using reversed() function:")
print(''.join(reversed(text)))

print("\nReversed using loop:")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)
