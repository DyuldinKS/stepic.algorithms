def merge_counting_inversions(a, b):
    i, j = 0, 0
    merged = []
    inversions = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
            inversions += len(a) - i

    merged.extend(a[i::] if i < len(a) else b[j::])
    return merged, inversions


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
