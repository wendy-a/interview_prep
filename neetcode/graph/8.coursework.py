from collections import defaultdict
from typing import List


def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # convert prerequisites to a map with class and prerequisite class
    # iterate the graph to find if a loop happens

    def find_loop(c):
        # base case
        if visited[c] == 1:
            return False
        if visited[c] == -1:
            return True
        # action at node
        visited[c] = -1

        res = False
        # iterate child
        for nextc in course_map[c]:
            if find_loop(nextc):
                return True
        visited[c] = 1  # c is not in a loop
        return False

    # initialize the map, course -> next available courses
    course_map = defaultdict(list)
    for a, b in prerequisites:
        course_map[b].append(a)

    # iterate the key of course map
    visited = [0 for _ in range(numCourses)]
    for course in list(course_map):
        if find_loop(course):
            return False
    return True