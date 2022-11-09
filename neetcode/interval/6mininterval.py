import heapq
from typing import List


def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()
    res = {}
    heap = []
    i = 0
    for val in sorted(queries):
        # put interval into pq, skip if all valid interval are in heap.
        while i < len(intervals) and intervals[i][0] <= val:
            start = intervals[i][0]
            end = intervals[i][1]
            # skip the interval if end < val
            if val <= end:
                heapq.heappush(heap, [end - start + 1, end])
            i += 1
        # remove bad solution, get possible solution
        while heap and heap[0][1] < val:
            heapq.heappop(heap)
        res[val] = heap[0][0] if heap else -1
    return [res[val] for val in queries]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minInterval([[4, 5], [5, 8], [1, 9], [8, 10], [1, 6]], [7, 9, 3, 9, 3]))
