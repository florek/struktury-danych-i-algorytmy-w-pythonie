def sort_selection(list):
    for run in range(len(list)):
        min_index = run
        for i in range(run + 1, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        list[run], list[min_index] = list[min_index], list[run]
        print(list)
    return list


print(sort_selection([2, 4, 7, 1, 3, 10]))