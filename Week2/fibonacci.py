n = 5
a, b = 0, 1

print(f"Fibonacci series till {n}th term:")
print(a)
print(b)

for i in range(2, n):
    c = a + b
    print(c)
    a, b = b, c
