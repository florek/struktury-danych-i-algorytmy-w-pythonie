def divide(arr, start, end):
    print("\n==============================")
    print(f"DIVIDE start={start}, end={end}")
    print(f"Lista na wejściu: {arr}")
    i = start
    pivot = arr[end]
    print(f"Pivot (arr[{end}]): {pivot}")
    for j in range(start, end):
        print(f"\nPorównuję arr[{j}]={arr[j]} <= pivot={pivot}?")
        if arr[j] <= pivot:
            print(f"TAK → swap arr[{i}]={arr[i]} z arr[{j}]={arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Lista po swapie: {arr}")
            i += 1
            print(f"i przesunięte na {i}")
        else:
            print("NIE → nic nie robię")
    print(f"\nKOŃCOWY swap pivotu:")
    print(f"swap arr[{i}]={arr[i]} z arr[{end}]={arr[end]}")
    arr[i], arr[end] = arr[end], arr[i]
    print(f"Lista po ustawieniu pivotu: {arr}")
    print(f"Pivot trafił na indeks {i}")
    print("==============================\n")
    return i


def quick_sort(arr, start, end):
    print(f"quick_sort(start={start}, end={end})")
    if start < end:
        border_index = divide(arr, start, end)
        quick_sort(arr, start, border_index - 1)
        quick_sort(arr, border_index + 1, end)
    else:
        print(f"STOP (start={start}, end={end})")


x = [2, 3, 1, 4]
quick_sort(x, 0, len(x) - 1)
print("\nWYNIK KOŃCOWY:", x)
