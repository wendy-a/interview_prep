def searchword(search_word, result_word):
    result_index = 0
    for curr_char in search_word:
        if curr_char == result_word[result_index]:
            result_index += 1
    return len(result_word) - result_index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(searchword('armaze', 'amazon'))
