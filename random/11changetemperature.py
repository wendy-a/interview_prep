def change_temperature(temp_change):
    prefix_sum = []
    temp_sum = 0
    for temp in temp_change:
        temp_sum += temp
        prefix_sum.append(temp_sum)
    max_change = 0
    for i, value in enumerate(temp_change):
        prefix = prefix_sum[i]
        curr_max = max(prefix, temp_sum - prefix + value)
        max_change = max(curr_max, max_change)
    return max_change


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(change_temperature([6, -2, 5]))
