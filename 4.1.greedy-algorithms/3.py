# find unique natural summands of the given number


def count_terms(n):
    count = 1
    while n > 2 * count:
        n -= count
        count += 1

    return count


def print_terms(n, k):
    for i in range(1, k):
        print(i, end=' ')
    print(int(n - k * (k - 1) / 2))


n = int(input())
k = count_terms(n)
print(k)
print_terms(n, k)
