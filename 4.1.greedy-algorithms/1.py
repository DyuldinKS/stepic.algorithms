# find the minimal set of points
# where each point is contained in at least one segment
from collections import namedtuple


class SegmentList:
    def init(self):
        length = int(input())
        for i in range(0, length):
            coords = map(int, input().split(' '))
            self._segments_list.append(self.Segment._make(coords))

    def sort(self):
        self._segments_list.sort(key=lambda segment: segment.end)

    def print_list(self):
        print(self._segments_list)

    def get_points_set(self):
        points_set = set()
        i = 0
        length = len(self._segments_list)

        while(i < length):
            curr_end = self._segments_list[i].end
            i += 1
            while(i < length and self._segments_list[i].begin <= curr_end):
                i += 1
            points_set.add(curr_end)

        return points_set

    Segment = namedtuple('Segment', ['begin', 'end'])
    _segments_list = []


s = SegmentList()
s.init()
s.sort()
points = s.get_points_set()
print(len(points))
for point in points:
    print(point, end=' ')
