from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(numCourses)]
    degree = [0] * numCourses
    for course, pre_course in prerequisites:
        graph[pre_course].append(course)
        degree[course] += 1

    bfs_queue = [i for i in range(numCourses) if degree[i] == 0]
    output = []
    while bfs_queue:
        course = bfs_queue.pop()
        output.append(course)
        for next_course in graph[course]:
            degree[next_course] -= 1
            if degree[next_course] == 0:
                bfs_queue.append(next_course)
    return output if len(output) == numCourses else []