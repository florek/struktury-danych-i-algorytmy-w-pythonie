def search_linear(value, list):
    idx = 0
    found = False
    while not found and idx < len(list):
        if list[idx] == value:
            found = True
        else:
            idx += 1
    return idx if idx < len(list) else None


list = [1, 7, 3, 1, 2, 3, 5, 6]
print(search_linear(5, list))
print(search_linear(111, list))