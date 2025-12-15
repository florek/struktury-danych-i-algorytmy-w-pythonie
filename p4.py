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


divided_list = []

def sort_merge_2(list):
    list_len = len(list)
    sorted_list = []
    if list_len <= 1:
        sorted_list = list
    else:
        middle_point = list_len // 2
        list_left = sort_merge_2(list[:middle_point])
        list_right = sort_merge_2(list[middle_point:])
        sorted_list = _sort_merge_2(list_left, list_right)
    return sorted_list


def _sort_merge_2(list_left, list_right):
    idx_left = idx_right = 0
    result = []
    while idx_left < len(list_left) and idx_right < len(list_right):
        if list_left[idx_left] < list_right[idx_right]:
            result.append(list_left[idx_left])
            idx_left += 1
        else:
            result.append(list_right[idx_right])
            idx_right += 1
    result.extend(list_left[idx_left:])
    result.extend(list_right[idx_right:])
    return result


print(sort_merge_2([7, 2, 9, 1, 13, 3]))
