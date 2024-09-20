def fibonacci_sequence(num):
    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b  = b, a+b
    return fib_sequence

n = int(input("Enter number: "))
sequence = fibonacci_sequence(n)
print(f"the first {n} terms of the Fibonaccie_sequence are: {sequence}")