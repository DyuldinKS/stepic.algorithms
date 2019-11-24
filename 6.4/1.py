def merge_counting_inversions(a, b, invs = 0):
    merged = []

    while a and b:
        if a[-1] <= b[-1]:
            merged.append(b.pop())
        else:
            merged.append(a.pop())
            invs += len(b)

    merged.reverse()
    merged = (a or b) + merged

    return merged, invs


def count_inversions(xs):
    inversions = 0

    def merge_sort(ls):
        if (len(ls) == 1):
            return ls

        m = len(ls) // 2
        left = merge_sort(ls[:m:])
        right = merge_sort(ls[m::])
        merged, invs = merge_counting_inversions(left, right)

        nonlocal inversions
        inversions += invs
        return merged

    merge_sort(xs)
    return inversions


def main():
    _ = input()
    xs = list(map(int, input().split(' ')))
    print(count_inversions(xs))


if __name__ == "__main__":
    main()
