# Click

## Jak jest u nas używane:

W pliku 'llama_sample.py' jest użyte tak, że uruchamiając ten plik można z linii poleceń dodać informację, ile razy chcemy uruchomić llamę. Uruchamiając:

```bash
$ pdm run python llama_sample.py

```
llama zostanie uruchomiona dokładnie raz (tak zostało to ustawione).
Można też jeśli chcemy uruchomić np. 10 razy można to zrobić tak:

```bash
$ pdm run python llama_sample.py --count=10
```

## Do czego może się to przydać?

Możliwe, że przyda się, ponieważ w actions czy innym łatwiej jest czasem korzystać z linii poleceń jedynie, to umożliwia to.

## Dokumentacja:

https://click.palletsprojects.com/en/8.1.x/

## Wersja w pdm:

W pdm jest wersja >= 8.1 (najnowsza to 8.1.3)

