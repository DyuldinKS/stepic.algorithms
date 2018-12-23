class Heap_max:
    def __init__(self, iterable=None):
        if not iterable:
            return

        for item in iterable:
            self.insert(item)

    def _swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]

    def _get_parent_index(self, index):
        return (index - 1) >> 1 if index > 0 else None

    def _get_max_child_index(self, parent_index):
        left = parent_index * 2 + 1
        right = left + 1
        length = len(self.list)
        if left < length:
            if right < length:
                return left if self.list[left] > self.list[right] else right
            else:
                return left
        else:
            return None

    def sift_up(self, i=None):
        elem_index = i if i is not None else len(self.list) - 1
        parent_index = self._get_parent_index(elem_index)

        while (parent_index is not None and
                self.list[parent_index] < self.list[elem_index]):
            self._swap(parent_index, elem_index)
            elem_index = parent_index
            parent_index = self._get_parent_index(elem_index)

    def sift_down(self, parent_index=0):
        child_index = self._get_max_child_index(parent_index)

        while (child_index is not None and
                self.list[parent_index] < self.list[child_index]):
            self._swap(parent_index, child_index)
            parent_index = child_index
            child_index = self._get_max_child_index(parent_index)

    def insert(self, elem):
        self.list.append(elem)
        self.sift_up()

    def extract_max(self):
        if len(self.list) == 1:
            return self.list.pop()
        parent_index = 0
        max_elem = self.list[parent_index]
        self.list[parent_index] = self.list.pop()
        self.sift_down()

        return max_elem

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return len(self.list) == 0

    def __str__(self):
        return str(self.list)

    list = []


def read_comands():
    comands_left = int(input())
    comands = []
    while comands_left:
        comands.append(input())
        comands_left -= 1

    return comands


def run(comands):
    heap = Heap_max()

    for cmd in comands:
        if cmd.startswith('Insert'):
            heap.insert(int(cmd.split(' ')[1]))
        else:
            print(heap.extract_max())


run(read_comands())
