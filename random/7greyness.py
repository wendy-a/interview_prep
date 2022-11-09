def greyness(map):
    rowGrey = [0] * len(map)
    colGrey = [0] * len(map[0])

    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == '1':
                rowGrey[row] += 1
                colGrey[col] += 1
            else:
                rowGrey[row] -= 1
                colGrey[col] -= 1
    return max(rowGrey) + max(colGrey)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(greyness(['1101', '0101', '1010']))
