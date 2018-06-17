from collections import Counter
from heap import Heap
from functools import total_ordering


# val with reversed frequency comparison
@total_ordering
class Node():
    def __init__(self, val='', freq=0):
        self.val = val
        self.freq = freq

    def __add__(self, other):
        return Node(self.val + other.val, self.freq + other.freq)

    def __eq__(self, other):
        return self.freq == other.freq

    def __ne__(self, other):
        return self.freq != other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __str__(self):
        return 'v: ' + self.val + '; f: ' + str(self.freq) + \
            '; left: ' + repr(self.left) + '; right ' + repr(self.right)

    def __repr__(self):
        return self.val + '-' + str(self.freq)


def gen_heap(items):
    heap = Heap()
    for (char, freq) in items:
        heap.insert(Node(char, freq))

    return heap


def use_prefix(codes, node, prefix):
    for char in node.val:
        codes[char] = prefix + (codes.get(char) or '')


def gen_codes(heap):
    codes = {}
    while len(heap) > 1:
        parent = Node()
        for i in range(0, 2):
            node = heap.extract_min()
            parent += node
            use_prefix(codes, node, str(i))

        heap.insert(parent)

    chars = heap.extract_min().val
    if len(chars) == 1:
        codes[chars] = '0'

    return codes


def huffman(s):
    assert(len(s) > 0)

    frequencies = Counter(s)
    chars = frequencies.items()
    heap = gen_heap(chars)
    codes = gen_codes(heap)
    res = ''.join(codes[char] for char in s)

    print(len(codes), len(res))
    [print('{}: {}'.format(k, codes[k])) for k in codes]
    print(res)


s = input()
huffman(s)
