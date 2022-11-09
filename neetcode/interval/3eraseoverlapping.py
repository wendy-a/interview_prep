from typing import List


def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    res = 0
    currend = intervals[0][1]
    for interval in intervals[1:]:
        if interval[0] >= currend:
            currend = interval[1]
        else:
            res += 1
            currend = min(interval[1], currend)

    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(eraseOverlapIntervals([[1, 3], [6, 9]]))
