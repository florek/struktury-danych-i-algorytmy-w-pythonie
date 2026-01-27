def search_interpolation(value, list):
    start = 0
    end = len(list) - 1
    found = False
    while start <= end and not found:
        if list[end] == list[start]:
            if list[start] == value:
                mid = start
                found = True
            else:
                break
        else:
            mid = int(start + (end - start) * (value - list[start]) / (list[end] - list[start]))
            if mid < start or mid > end:
                break
            if list[mid] == value:
                found = True
            else:
                if value < list[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
    if found:
        return mid
    else:
        return None


list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 5
idx = search_interpolation(value, list)
print(f'Index of {value} is {idx}')
