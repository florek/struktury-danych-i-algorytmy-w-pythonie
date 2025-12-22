# Algorithms Handbook – podstawy sortowania (Python)

Ten dokument jest **edukacyjnym handbookiem**, którego celem jest:
- zrozumienie *jak działają algorytmy sortowania*,
- wyrobienie **modelu mentalnego**, a nie zapamiętywanie kodu,
- umiejętność debugowania i tłumaczenia algorytmów „na głos”.

Każdy algorytm zawiera:
- kod,
- opis krok po kroku,
- właściwości obliczeniowe,
- kiedy i dlaczego go używać.

---

## 1. Zamiana wartości zmiennych (Python idiom)

```python
x = 1
y = 100
x, y = y, x
```

### Co tu się dzieje

Python pozwala na **jednoczesne przypisanie wielu wartości**.
Pod spodem tworzona jest krotka tymczasowa, dzięki czemu:

- nie potrzebujesz zmiennej pomocniczej,
- operacja jest czytelna i bezpieczna,
- idiom jest powszechnie używany w sortowaniach.

### Do zapamiętania

* idiom Pythona
* zero boilerplate
* idealny do algorytmów in-place

---

## 2. Bubble Sort – wersja podstawowa

Bubble Sort to najprostszy algorytm sortowania.
Polega na **wielokrotnym przechodzeniu po liście** i zamienianiu sąsiednich elementów.

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

### Jak to działa mentalnie

- największe elementy „wypływają” na koniec listy
- każda iteracja skraca obszar chaosu
- brak zamian = lista posortowana

### Właściwości

* czas: **O(n²)**
* stabilny
* in-place
* bardzo wolny – tylko edukacyjnie

---

## 3. Insertion Sort

Insertion Sort działa jak **sortowanie kart w ręce**.

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

### Model mentalny

- lewa część listy jest zawsze posortowana
- jeden element jest „wstawiany” w dobre miejsce
- przesuwasz elementy w prawo, aż znajdziesz lukę

### Właściwości

* czas: **O(n²)**, najlepszy: **O(n)**
* stabilny
* in-place
* świetny dla małych lub prawie posortowanych danych

---

## 4. Selection Sort

Selection Sort polega na **wybieraniu minimum** z nieposortowanej części.

```python
def sort_selection(list):
    for run in range(len(list)):
        min_index = run
        for i in range(run + 1, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        list[run], list[min_index] = list[min_index], list[run]
```

### Jak myśleć

- dzielisz listę na posortowaną i nieposortowaną
- zawsze szukasz minimum
- wykonujesz dokładnie jeden swap na iterację

### Właściwości

* czas: **O(n²)**
* niestabilny
* in-place
* mało swapów, dużo porównań

---

## 5. Merge Sort – idea

Merge Sort to algorytm **dziel i zwyciężaj**.

> Kluczowa prawda:
> **Merge Sort nie sortuje list – on sortuje DWIE LISTY.**

Rekurencja służy tylko do dostarczenia danych.

---

## 6. Merge Sort – wersja edukacyjna (z debugiem)

```python
def sort_merge(list):
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    left = sort_merge(list[:middle])
    right = sort_merge(list[middle:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Co tu obserwować

- rekurencja NIC nie sortuje
- sortowanie zachodzi wyłącznie w scalaniu
- zawsze pracujesz na już posortowanych danych

---

## 7. Merge Sort – właściwości

* czas: **O(n log n)**
* pamięć: **O(n)**
* stabilny
* przewidywalny

---

## 8. Quick Sort – idea

Quick Sort działa odwrotnie niż Merge Sort.

- nie scala
- ustawia **jeden element (pivot)**
- resztę zostawia rekurencji

---

## 9. Quick Sort – wersja edukacyjna

```python
def divide(arr, start, end):
    pivot = arr[end]
    i = start

    for j in range(start, end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[end] = arr[end], arr[i]
    return i


def quick_sort(arr, start, end):
    if start < end:
        p = divide(arr, start, end)
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)
```

### Model mentalny

- pivot trafia na swoje miejsce
- elementy mniejsze są po lewej
- większe po prawej
- rekurencja robi resztę

---

## 10. Quick Sort – właściwości

* średni czas: **O(n log n)**
* najgorszy: **O(n²)**
* in-place
* niestabilny

---

## 11. Podsumowanie

| Algorytm | Czas | Pamięć | Stabilność |
|--------|------|--------|------------|
| Bubble | n² | 1 | ✅ |
| Insertion | n² | 1 | ✅ |
| Selection | n² | 1 | ❌ |
| Merge | n log n | n | ✅ |
| Quick | n log n | log n | ❌ |

---

## 12. Najważniejsze wnioski

* algorytmy sortowania uczą myślenia
* rekurencja to logistyka
* scalanie i pivot to sedno
* rozumienie > zapamiętywanie

# Algorytmy – wyszukiwanie liniowe (Linear Search)

## 1. Definicja

**Wyszukiwanie liniowe** (linear search) to najprostszy algorytm wyszukiwania elementu w liście.  
Polega na **sprawdzaniu kolejnych elementów jeden po drugim**, aż do znalezienia wartości lub końca listy.

---

## 2. Implementacja

```python
def search_linear(value, list):
    idx = 0
    found = False
    while not found and idx < len(list):
        if list[idx] == value:
            found = True
        else:
            idx += 1
    return idx if idx < len(list) else None
