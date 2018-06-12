# find the reminder of the n-th Fibonacci number devision


def fib_reminder(n, div):
    cache = [0, 1]
    for i in range(2, n + 1):
        cache.append((cache[-2] + cache[-1]) % div)
        # use the Pisano period
        if(cache[-2] == 0 and cache[-1] == 1):
            cache = cache[:-2]
            break
    return cache[n % len(cache)]


n, m = map(int, input().split(' '))
print(fib_reminder(n, m))
