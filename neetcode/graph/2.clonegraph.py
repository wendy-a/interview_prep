class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    visited_map = {}

    # return copy of input node
    def dfs(node):
        # base case
        if not node:
            return None

        if node in visited_map:
            return visited_map[node]

            # action at node
        copy = Node(node.val, None)
        visited_map[node] = copy

        # get sub array
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        # return final copy
        return copy

    return dfs(node)
