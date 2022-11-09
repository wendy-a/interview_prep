from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
