from typing import List
# Leetcode 435

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    counter = 0
    end = -float('inf')
    for i in sorted(intervals, key=lambda interval: interval[1]):
        if i[0] >= end:
            end = i[1]
        else:
            counter += 1
    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(eraseOverlapIntervals([[-52, 31], [-73, -26], [82, 97], [-65, -11],
                                 [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98],
                                 [-63, 2], [30, 47], [-40, -26]]))


