## Instalacja:

```bash
pip install -U pytest
```

## Dokumentacja:

https://docs.pytest.org/en/8.0.x/index.html

## Uruchamianie testu: 

```bash
pytest 
```

**ważne**: trzeba być w 'LLM-supported-review-system/Research$', inaczej na razie będzie wywalać, bo nie ma jeszcze testów w pozostałych plikach pythonowych

oczywiście ostateczie zostanie to naprawione, ale na razie jest jak jest

## Wynik:

jeśli przechodzi dostajemy:
![PASSED](image-1.png)

a jeśli nie, to:
![FAILED](image.png)

## Dodatkowe info:

1. pytest sprawdza wszystkie pliki test_*.py i *_test.py, dlatego uruchamia test_sample.py oraz test_llama.py
2. można jeszcze jakieś fajne rzeczy z przechwytywaniem errorów czy innych robić, potem dorzucę do kodu przykłady(na razie jest coś co działa i nawet sprawdza coś sensownego)
3. dokumentacja jest fajna i czytelna, więc w razie pytań polecam
4. Na ten moment jest sprawdzanie, czy dostaniemy niepustą odpowiedź od ollamy na zapytanie 'hi!'

