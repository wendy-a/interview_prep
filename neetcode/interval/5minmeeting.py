from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    start = [i[0] for i in intervals]
    end = [i[1] for i in intervals]
    start.sort()
    end.sort()
    curr = 0
    res = 0
    n = len(intervals)
    i, j = 0, 0
    while i < n and j < n:
        if start[i] < end[j]:
            curr += 1
            i += 1
        else:
            curr -= 1
            j += 1
        res = max(curr, res)
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
