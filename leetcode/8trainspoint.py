def trainpot(k, exist):
    rest = k - len(exist)
    count = 1
    for i in range(rest):
        if count in exist:
            while count in exist:
                count += 1
        count += 1
    return count - 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(trainpot(10,[2,5]))
