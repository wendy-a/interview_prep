from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for index, interval in enumerate(intervals):
        # append interval before new interval
        if interval[1] < newInterval[0]:
            res.append(interval)
        # append new interval if it happens before current interval.
        elif interval[0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[index:]
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

    res.append(newInterval)

    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(insert([[1, 3], [6, 9]], [2, 5]))
