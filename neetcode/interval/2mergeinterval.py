from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []
    intervals = sorted(intervals)
    ready = intervals[0]
    for i in range(1, len(intervals)):
        if ready[1] < intervals[i][0]:
            res.append(ready)
            ready = intervals[i]
        elif ready[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            ready[0] = min(ready[0], intervals[i][0])
            ready[1] = max(ready[1], intervals[i][1])
    res.append(ready)
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(merge([[1, 3], [6, 9]]))
