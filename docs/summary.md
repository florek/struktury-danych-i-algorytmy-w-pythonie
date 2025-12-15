# Algorithms Handbook – podstawy sortowania (Python)

---

## 1. Zamiana wartości zmiennych (Python idiom)

```python
x = 1
y = 100
x, y = y, x
```

### Do zapamiętania

* idiom Pythona
* często używany w algorytmach sortowania

---

## 2. Bubble Sort – wersja podstawowa

```python
def sort_bubble(list):
    is_change = True
    while is_change:
        is_change = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_change = True
```

---

## 3. Insertion Sort

```python
def sort_insert(list):
    for sort_border in range(1, len(list)):
        curr_idx = sort_border - 1
        value = list[curr_idx + 1]
        while curr_idx >= 0 and list[curr_idx] > value:
            list[curr_idx + 1] = list[curr_idx]
            curr_idx -= 1
        list[curr_idx + 1] = value
```

---

## 4. Selection Sort

```python
def sort_selection(list):
    for run in range(len(list)):
        min_index = run
        for i in range(run + 1, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        list[run], list[min_index] = list[min_index], list[run]
```

---

## 5. Merge Sort – wersja EDUKACYJNA (z debugiem)

> ⚠️ Ta wersja **nie jest do produkcji**. Jest po to, żeby **zobaczyć moment sortowania**.

```python
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

    return sorted_list
```

### Co tu obserwować

* **dzielenie nic nie sortuje**
* sortowanie zachodzi **wyłącznie w pętli while**
* zawsze scalane są **DWIE już posortowane listy**

---

## 6. Merge Sort – wersja CZYSTA (produkcja)

> Ten wariant **oddziela rekurencję od scalania** – to jest właściwy model mentalny.

```python
def sort_merge_2(list):
    list_len = len(list)
    if list_len <= 1:
        return list

    middle_point = list_len // 2
    list_left = sort_merge_2(list[:middle_point])
    list_right = sort_merge_2(list[middle_point:])

    return _sort_merge_2(list_left, list_right)


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
```

```python
print(sort_merge_2([7, 2, 9, 1, 13, 3]))
```

### Dlaczego ta wersja jest lepsza

* **rekurencja = logistyka**
* **_sort_merge_2 = prawdziwy algorytm**
* łatwo testować, łatwo debugować

---

## 7. Najważniejszy mentalny model (KRYTYCZNE)

> **Merge Sort NIE sortuje list.**
> **Merge Sort sortuje TYLKO DWIE LISTY.**

Rekurencja służy wyłącznie do tego, aby:

* dostać dwie mniejsze listy
* które są już posortowane

---

## 8. Właściwości Merge Sort

* czas: **O(n log n)** (zawsze)
* pamięć: **O(n)**
* stabilny
* nie in-place

---

## 9. TL;DR – Merge Sort

* dzielenie ≠ sortowanie
* sortowanie dzieje się **przy scalaniu**
* `_sort_merge_2()` to serce algorytmu
* rekurencja to tylko dostarczanie danych
* jeśli rozumiesz scalanie → rozumiesz w
