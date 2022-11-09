def how_many(s, t):
    s_dict = {}
    t_dict = {}
    res = len(t)
    for s_char in s:
        s_dict[s_char] = 1 if s_char not in s_dict else s_dict.get(s_char) + 1
    for t_char in t:
        t_dict[t_char] = 1 if t_char not in t_dict else t_dict.get(t_char) + 1
    for t_char in t_dict:
        time = s_dict.get(t_char, 0)//t_dict.get(t_char)
        res = min(time, res)
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(how_many('mononom', 'mon'))
    print(how_many('abacbc', 'bca'))
