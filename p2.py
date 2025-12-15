def sort_insert(list):
    for sort_border in range(1, len(list)):
        curr_idx = sort_border - 1
        value = list[curr_idx + 1]
        while list[curr_idx] > value and curr_idx >= 0:
            list[curr_idx + 1] = list[curr_idx]
            curr_idx = curr_idx - 1
        list[curr_idx + 1] = value
        print(f'Debug {sort_border} - {list}')


sort_insert([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
