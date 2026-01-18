def search_binary(value, list):
    start = 0
    end = len(list) - 1
    found = False
    while start <= end and not found:
        print(f'DEBUG: start={start}, end={end}')
        mid = (start + end) // 2
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
idx = search_binary(value, list)
print(f'Index of {value} is {idx}')
