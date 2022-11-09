def primemovieaward(k, award):
    sorted_award = sorted(award)
    count = 1
    min = sorted_award[0]
    for value in sorted_award:
        if value - min < k:
            continue
        else:
            min = value
            count+=1
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(primemovieaward(3,[1,5,4,6,8,9,2]))
