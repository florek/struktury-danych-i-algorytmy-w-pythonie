def sort_merge(list):
    list_len = len(list)
    sorted_list = []
    if list_len <= 1:
        sorted_list = list
    else:
        middle_point = list_len // 2
        list_left = sort_merge(list[:middle_point])
        list_right = sort_merge(list[middle_point:])
        print(f'LL: {list_left} / LR: {list_right}')
        idx_left = idx_right = 0
        while idx_left < len(list_left) and idx_right < len(list_right):
            if list_left[idx_left] < list_right[idx_right]:
                sorted_list.append(list_left[idx_left])
                idx_left += 1
            else:
                sorted_list.append(list_right[idx_right])
                idx_right += 1
            print(f'sorted_list: {sorted_list}')
        sorted_list.extend(list_left[idx_left:])
        sorted_list.extend(list_right[idx_right:])
        print(f'sorted_list_extended: {sorted_list}')
    # print(f'DEBUG: {list} -> {sorted_list}')
    return sorted_list

print(sort_merge([7, 2, 9, 1, 13, 3]))
