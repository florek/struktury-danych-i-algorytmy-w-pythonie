x = 1
y = 100
x, y = y, x
print(x, y)


def sort_bubble(list):
    is_change = True
    while is_change:
        is_change = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_change = True

x = [1, 3, 2, 9, 7, 3, 2]
sort_bubble(x)
print(x)


def sort_bubble2(list):
    max_index = len(list) - 1
    for max_not_sorted_index in range(max_index, 0, -1):
        is_change = False
        for i in range(max_not_sorted_index):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_change = True
        if not is_change:
            break

x = [1, 3, 2, 9, 7, 3, 2]
sort_bubble2(x)
print(x)
