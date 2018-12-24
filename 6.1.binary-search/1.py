def init():
    _, *l1 = map(int, input().split(' '))
    search_in = sorted(enumerate(l1), key=lambda x: x[1])
    _, *search_each_of = enumerate(map(int, input().split(' ')))
    return (search_in, search_each_of) 

def binary_search(enmr, x, start, end):
    if (start >= end):
        return -1
    center = (start + end) // 2
    if x > enmr[center][1]:
        return binary_search(enmr, x, center + 1, end)
    if x < enmr[center][1]:
        return binary_search(enmr, x, start, center)
    return enmr[center][0] + 1

search_in, search_each_of = init()
res = " ".join(map(
    lambda x: str(binary_search(search_in, x[1], 0, len(search_in))),
    search_each_of))

print(res)