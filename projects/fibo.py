# Print Fibonacci series up to n
n = 10  # You can change this to any number
a, b = 0, 1
while a < n:
    print(a, end=' ')
    a, b = b, a + b
print()

# Create a list of Fibonacci numbers up to n
n = 10  # You can change this as needed
result = []
a, b = 0, 1
while a < n:
    result.append(a)
    a, b = b, a + b

print(result)
