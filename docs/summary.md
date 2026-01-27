# Algorithms Handbook – sortowanie i wyszukiwanie (Python)

Ten dokument jest **edukacyjnym handbookiem**, którego celem jest:
- zrozumienie *jak działają algorytmy sortowania i wyszukiwania*,
- wyrobienie **modelu mentalnego**, a nie zapamiętywanie kodu,
- umiejętność debugowania i tłumaczenia algorytmów „na głos".

Każdy algorytm zawiera:
- kod,
- opis krok po kroku,
- właściwości obliczeniowe,
- kiedy i dlaczego go używać,
- przykłady wykonania krok po kroku.

---

## Struktura projektu

Projekt zawiera następujące pliki z implementacjami algorytmów:

### Sortowanie

- **[p1.md](p1.md)** - Bubble Sort (zamiana wartości, wersja podstawowa i zoptymalizowana)
- **[p2.md](p2.md)** - Insertion Sort
- **[p3.md](p3.md)** - Selection Sort
- **[p4.md](p4.md)** - Merge Sort
- **[p5.md](p5.md)** - Quick Sort

### Wyszukiwanie

- **[p6.md](p6.md)** - Linear Search (Wyszukiwanie liniowe)
- **[p7.md](p7.md)** - Binary Search (Wyszukiwanie binarne)
- **[p8.md](p8.md)** - Interpolation Search (Wyszukiwanie interpolacyjne)

---

## Podsumowanie algorytmów sortowania

| Algorytm | Czas | Pamięć | Stabilność | Plik |
|--------|------|--------|------------|------|
| Bubble | n² | 1 | ✅ | [p1.md](p1.md) |
| Insertion | n² | 1 | ✅ | [p2.md](p2.md) |
| Selection | n² | 1 | ❌ | [p3.md](p3.md) |
| Merge | n log n | n | ✅ | [p4.md](p4.md) |
| Quick | n log n | log n | ❌ | [p5.md](p5.md) |

---

## Podsumowanie algorytmów wyszukiwania

| Algorytm | Czas | Wymagania | Kiedy używać | Plik |
|--------|------|-----------|--------------|------|
| Linear Search | O(n) | brak | małe listy, nieposortowane dane | [p6.md](p6.md) |
| Binary Search | O(log n) | lista posortowana | duże zbiory, częste wyszukiwania | [p7.md](p7.md) |
| Interpolation Search | O(log log n) | lista posortowana, równomierny rozkład | bardzo duże zbiory, równomiernie rozłożone dane | [p8.md](p8.md) |

---

## Najważniejsze wnioski – sortowanie

* algorytmy sortowania uczą myślenia
* rekurencja to logistyka
* scalanie i pivot to sedno
* rozumienie > zapamiętywanie

---

## Najważniejsze wnioski – wyszukiwanie

* wyszukiwanie liniowe jest uniwersalne, ale wolne
* wyszukiwanie binarne jest szybkie, ale wymaga posortowania
* wyszukiwanie interpolacyjne jest najszybsze dla równomiernie rozłożonych danych
* wybór algorytmu zależy od kontekstu i częstotliwości wyszukiwań
* sortowanie raz + wiele wyszukiwań binarnych często lepsze niż wiele wyszukiwań liniowych
