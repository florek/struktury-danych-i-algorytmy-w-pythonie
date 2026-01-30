def quick_select(arr, k):
    if k < 1 or k > len(arr):
        return None
    return _quick_select(arr, 0, len(arr) - 1, k - 1)


def _partition(arr, left, right):
    pivot_idx = right
    pivot_value = arr[pivot_idx]
    store_idx = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_idx], arr[i] = arr[i], arr[store_idx]
            store_idx += 1
    arr[store_idx], arr[pivot_idx] = arr[pivot_idx], arr[store_idx]
    return store_idx


def _quick_select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_idx = _partition(arr, left, right)
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return _quick_select(arr, left, pivot_idx - 1, k)
    else:
        return _quick_select(arr, pivot_idx + 1, right, k)


arr = [7, 10, 4, 3, 20, 15]
k = 3
result = quick_select(arr.copy(), k)
print(f'{k}-ty najmniejszy element w {arr} to {result}')

arr2 = [7, 10, 4, 3, 20, 15]
k2 = 1
result2 = quick_select(arr2.copy(), k2)
print(f'{k2}-ty najmniejszy element w {arr2} to {result2}')

arr3 = [7, 10, 4, 3, 20, 15]
k3 = 6
result3 = quick_select(arr3.copy(), k3)
print(f'{k3}-ty najmniejszy element w {arr3} to {result3}')
