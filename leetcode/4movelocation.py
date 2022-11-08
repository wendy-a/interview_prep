def move_location(locations, moved_from, moved_to):
    location_set = set(locations)
    for i, from_val in enumerate(moved_from):
        location_set.remove(from_val)
        location_set.add(moved_to[i])
    return sorted(location_set)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(move_location([1, 7, 6, 8], [1, 7, 2], [2, 9, 5]))
