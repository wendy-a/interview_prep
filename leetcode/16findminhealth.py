from typing import List


# leetcode 2214
def minimumHealth(damage: List[int], armor: int) -> int:
    return 1 + sum(damage) - min(max(damage), armor)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minimumHealth([2, 7, 4, 3], 4))
