class Heap:
    def __init__(self, iterable=None):
        if not iterable:
            return

        for item in iterable:
            self.insert(item)

    def _swap(self, i, j):
        self.list[i], self.list[j] = self.list[j], self.list[i]

    def _get_parent_index(self, index):
        return (index - 1) >> 1 if index > 0 else None

    def _get_min_child_index(self, parent_index):
        left = parent_index * 2 + 1
        right = left + 1
        length = len(self.list)
        if left < length:
            if right < length:
                return left if self.list[left] <= self.list[right] else right
            else:
                return left
        else:
            return None

    def insert(self, elem):
        elem_index = len(self.list)
        self.list.append(elem)
        parent_index = self._get_parent_index(elem_index)

        while (parent_index is not None and
                self.list[parent_index] > self.list[elem_index]):
            self._swap(parent_index, elem_index)
            elem_index = parent_index
            parent_index = self._get_parent_index(elem_index)

    def extract_min(self):
        if len(self.list) == 1:
            return self.list.pop()
        parent_index = 0
        min_elem = self.list[parent_index]
        self.list[parent_index] = self.list.pop()
        child_index = self._get_min_child_index(parent_index)

        while (child_index is not None and
                self.list[parent_index] > self.list[child_index]):
            self._swap(parent_index, child_index)
            parent_index = child_index
            child_index = self._get_min_child_index(parent_index)

        return min_elem

    def len(self):
        return len(self.list)

    def is_empty(self):
        return len(self.list) == 0

    def __str__(self):
        return str(self.list)

    list = []
