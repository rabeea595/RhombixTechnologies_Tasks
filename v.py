def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # Update values for the next iteration

# Example: Generate the first 10 Fibonacci numbers
fib = fibonacci_generator()
for _ in range(100):
    print(next(fib), end=" ")
