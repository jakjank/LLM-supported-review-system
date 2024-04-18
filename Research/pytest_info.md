## Instalacja:

```bash
pip install -U pytest
```

## Dokumentacja:

https://docs.pytest.org/en/8.0.x/index.html

## Uruchamianie testu: 
Należy być w /project

```bash
pdm run pytest
```

!!! UWAGA !!!
może ten test trwać bardzo długo - trwa znacznie dłużej niż odpalany lokalnie, ale działa (warto być cierpliwym)

## Wynik:
przykładowy poprawny wynik:
![przyklad_unady_test_ollama](https://github.com/jakjank/LLM-supported-review-system/assets/116657891/c4414c03-a079-4ac3-9860-d44c45a911fd)


## Dodatkowe info:

1. pytest sprawdza wszystkie pliki test_*.py i *_test.py, dlatego uruchamia test_sample.py oraz test_llama.py
2. można jeszcze jakieś fajne rzeczy z przechwytywaniem errorów czy innych robić, potem dorzucę do kodu przykłady(na razie jest coś co działa i nawet sprawdza coś sensownego)
3. dokumentacja jest fajna i czytelna, więc w razie pytań polecam
4. Na ten moment jest sprawdzanie, czy dostaniemy niepustą odpowiedź od ollamy na zapytanie 'hi!'

