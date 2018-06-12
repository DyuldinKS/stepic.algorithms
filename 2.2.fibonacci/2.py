# find the last digit of the n-th Fibonacci number


def fibonacci(n):
    if not n:
        return 0
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# final digits of the Fibonacci numbers recur after a cycle of 60
n = int(input())
print(fibonacci(n % 60) % 10)
