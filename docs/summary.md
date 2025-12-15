# Algorithms Handbook – podstawy sortowania (Python)

---

## 1. Zamiana wartości zmiennych (Python idiom)

```python
x = 1
y = 100
x, y = y, x
```

### Co tu się dzieje

* Python umożliwia **równoczesne przypisanie**
* Nie jest tworzona zmienna tymczasowa

### Do zapamiętania

* to jest idiom Pythona
* często używany w algorytmach (np. sortowanie)

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

### Idea algorytmu

* porównuje **sąsiednie elementy**
* największe wartości „wypływają” na koniec listy
* powtarza przebiegi, aż nie będzie zmian

### Właściwości

* czas: **O(n²)**
* pamięć: **O(1)** (in-place)
* stabilny

---

## 3. Bubble Sort – wersja zoptymalizowana

```python
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
```

### Co jest lepsze

* każda iteracja skraca zakres sortowania
* wcześniejsze zakończenie, jeśli lista jest już posortowana

### Wniosek

* nadal **O(n²)**, ale szybszy w praktyce

---

## 4. Insertion Sort (sortowanie przez wstawianie)

```python
def sort_insert(list):
    for sort_border in range(1, len(list)):
        curr_idx = sort_border - 1
        value = list[curr_idx + 1]
        while curr_idx >= 0 and list[curr_idx] > value:
            list[curr_idx + 1] = list[curr_idx]
            curr_idx = curr_idx - 1
        list[curr_idx + 1] = value
```

### Idea algorytmu

* lista jest dzielona na:

  * część posortowaną
  * część nieposortowaną
* każdy nowy element jest **wstawiany w odpowiednie miejsce**

### Właściwości

* czas: **O(n²)** (najgorszy przypadek)
* bardzo szybki dla:

  * małych list
  * list prawie posortowanych
* stabilny

---

## 5. Selection Sort (sortowanie przez wybór)

```python
def sort_selection(list):
    for run in range(len(list)):
        min_index = run
        for i in range(run + 1, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        list[run], list[min_index] = list[min_index], list[run]
```

### Idea algorytmu

* w każdej iteracji:

  * szuka najmniejszego elementu
  * zamienia go z bieżącą pozycją

### Właściwości

* czas: **O(n²)** (zawsze)
* pamięć: **O(1)**
* niestabilny
* prosty do zrozumienia, rzadko używany w praktyce

---

## 6. Merge Sort (sortowanie przez scalanie)

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

        idx_left = idx_right = 0
        while idx_left < len(list_left) and idx_right < len(list_right):
            if list_left[idx_left] < list_right[idx_right]:
                sorted_list.append(list_left[idx_left])
                idx_left += 1
            else:
                sorted_list.append(list_right[idx_right])
                idx_right += 1

        sorted_list.extend(list_left[idx_left:])
        sorted_list.extend(list_right[idx_right:])

    return sorted_list
```

### Idea algorytmu

* **dziel i zwyciężaj**:

  1. dzieli listę na połowy
  2. sortuje rekurencyjnie każdą połowę
  3. **scala** dwie posortowane listy w jedną

### Co tu jest kluczowe

* sortowanie **nie dzieje się przy dzieleniu**
* sortowanie następuje **podczas scalania**
* zawsze scalane są **dwie już posortowane listy**

### Właściwości

* czas: **O(n log n)** (zawsze)
* pamięć: **O(n)** (tworzy nowe listy)
* stabilny
* nie jest in-place

### Debugowanie (edukacyjne)

W wersji uczącej się często dodaje się `print()` aby zobaczyć:

* jak lista jest dzielona
* jak powstaje lista wynikowa krok po kroku

```python
print(sort_merge([7, 2, 9, 1, 13, 3]))
```

---

## 7. Porównanie algorytmów

| Algorytm       | Czas       | Stabilny | In-place |
| -------------- | ---------- | -------- | -------- |
| Bubble Sort    | O(n²)      | Tak      | Tak      |
| Insertion Sort | O(n²)      | Tak      | Tak      |
| Selection Sort | O(n²)      | Nie      | Tak      |
| Merge Sort     | O(n log n) | Tak      | Nie      |

---

## 8. Kiedy którego używać

* **Bubble Sort** – edukacja, zrozumienie idei
* **Insertion Sort** – małe / prawie posortowane dane
* **Selection Sort** – nauka algorytmów, nie produkcja
* **Merge Sort** – duże zbiory danych, przewidywalny czas

---

## 9. TL;DR – sortowanie

* Zamiana `a, b = b, a` to Python idiom
* Bubble Sort → prosty, wolny
* Insertion Sort → szybki dla małych danych
* Selection Sort → zawsze O(n²)
* Merge Sort → O(n log n), kosztem pamięci
* W praktyce → `sorted()` / `list.sort()`
