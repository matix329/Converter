# Currency Converter
---
## Opis projektu

Ten program to **przelicznik walut**, który pobiera aktualne kursy walut z publicznego API [Floatrates](http://www.floatrates.com/). Program zapisuje kursy walut w pamięci podręcznej (cache), aby zoptymalizować przyszłe przeliczenia i zmniejszyć liczbę zapytań do API. Dzięki temu możesz wielokrotnie przeliczać różne waluty bez potrzeby ponownego pobierania kursów.

### Kluczowe funkcje:
- Pobiera kursy walut na podstawie wybranej waluty źródłowej.
- Automatycznie zapisuje kursy dla walut **USD** i **EUR** w cache przy starcie programu.
- Użytkownik może wielokrotnie wprowadzać różne waluty docelowe i kwoty, a program automatycznie przelicza wartość na podstawie aktualnego kursu.
- Jeśli kurs waluty docelowej nie znajduje się w cache, jest pobierany na bieżąco z API i zapisywany do cache.
- Program obsługuje wiele walut i działa w trybie interaktywnym, dopóki użytkownik nie zakończy działania programu.

## Jak działa program?

1. Program pyta użytkownika o kod waluty źródłowej (np. **USD**, **EUR**, **PLN**).
2. Program wysyła żądanie do API Floatrates, aby pobrać aktualne kursy wymiany dla waluty źródłowej.
3. Kursy dla **USD** i **EUR** są automatycznie zapisywane w cache.
4. W trybie interaktywnym użytkownik wprowadza kolejne waluty docelowe, na które chce przeliczać podaną kwotę:
   - Jeśli kurs waluty docelowej jest już w cache, program go używa.
   - Jeśli kurs nie znajduje się w cache, program pobiera go z API i zapisuje do cache.
5. Program wyświetla przeliczoną wartość w walucie docelowej.
6. Proces trwa, dopóki użytkownik nie naciśnie "Enter", aby zakończyć działanie.

### Przykład działania:

```
> usd #waluta źródłowa
> eur #waluta docelowa
> 100 #kwota
Checking the cache...
Oh! It is in the cache!
You received 85.50 EUR.

> nok
> 200 #waluta docelowa
Checking the cache...
Sorry, but it is not in the cache!
You received 1872.45 NOK.
```

## Wymagania

- Python 3.x
- Biblioteka `requests`

## Użycie

Po uruchomieniu programu zostaniesz poproszony o wprowadzenie kodu waluty źródłowej (np. **usd**). Następnie możesz wprowadzać różne waluty docelowe i kwoty, które chcesz przeliczać. Program będzie przeliczał wartość na podstawie aktualnych kursów walut i wyświetlał wyniki na ekranie.

## Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.
