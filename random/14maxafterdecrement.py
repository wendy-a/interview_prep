#Leetcode 1846
def maxafterdecrement(arr):
    arr.sort()
    pre = 0
    for val in arr:
        pre = min(pre + 1, val)
    return pre


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maxafterdecrement([7, 3, 6, 1]))
