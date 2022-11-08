def jiu_gong_ge(input_string):
    if not input_string:
        return 0
    char_dict = {}
    for char in input_string:
        if char in char_dict:
            char_dict[char] = char_dict.get(char) + 1
        else:
            char_dict[char] = 1

    sorted_char_dict = sorted(char_dict, key=char_dict.get, reverse=True)

    counter = 0
    for index, value in enumerate(sorted_char_dict):
        counter += (char_dict[value] * (index//9 + 1))
    print(counter)
    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jiu_gong_ge('abacadefghibj')
