# pick up a backpack


from collections import namedtuple


class Backpack:
    def init(self):
        num_of_items, self._volume = map(int, input().split())
        for i in range(0, num_of_items):
            coords = map(int, input().split(' '))
            self._all_items.append(self.Item._make(coords))

    def sort(self):
        self._all_items.sort(key=lambda o: o.cost / o.weight, reverse=True)

    def pick_up(self):
        cost = 0
        rest_volume = self._volume
        for obj in self._all_items:
            if obj.weight > rest_volume:
                cost += (rest_volume / obj.weight) * obj.cost
                break
            cost += obj.cost
            rest_volume -= obj.weight
        return cost

    Item = namedtuple('Item', ['cost', 'weight'])
    _all_items = []


bp = Backpack()
bp.init()
bp.sort()
print(bp.pick_up())
