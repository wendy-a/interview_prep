def minsum(k, arr):
    prefix_sum = [0]
    arr_sum = 0
    for val in arr:
        arr_sum += val
        prefix_sum.append(arr_sum)
    res = float('inf')
    for i in range(len(arr) - k):
        sum_left = arr_sum - (prefix_sum[i + k] - prefix_sum[i])
        res = min(sum_left, res)
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minsum(2, [7, 3, 6, 1]))
