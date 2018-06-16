from collections import Counter
from heap import Heap
from functools import total_ordering


# val with reversed frequency comparison
@total_ordering
class Node():
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.left = None
        self.right = None

    def set_children(self, ch1, ch2=None):
        self.left = ch1
        self.right = ch2

    def is_leaf(self):
        return len(self.val) == 1

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


def build_tree(heap):
    while heap.len() > 1:
        c1 = heap.extract_min()
        c2 = heap.extract_min()
        parent = c1 + c2
        parent.set_children(c1, c2)
        heap.insert(parent)

    return heap.extract_min()


def gen_codes(node, code='', codes={}):
    if(node.left):
        gen_codes(node.left, code + '0', codes)

    if(node.right):
        gen_codes(node.right, code + '1', codes)

    if node.left == node.right and node.left is None:
        codes[node.val] = code or '0'

    return codes


def encode(s, codes):
    encoded = ''
    for char in s:
        encoded += codes[char]

    return encoded


def huffman(s):
    assert(len(s) > 0)

    frequencies = Counter(s)
    chars = frequencies.items()
    heap = gen_heap(chars)
    parent = build_tree(heap)
    codes = gen_codes(parent)
    res = encode(s, codes)

    print(len(codes), len(res))
    for (char, freq) in chars:
        print(char + ': ' + codes[char])
    print(res)


s = input()
huffman(s)
