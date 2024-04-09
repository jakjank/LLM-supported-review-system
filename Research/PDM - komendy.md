**INSTALACJA**
--------------

**LINUX!**

```text-plain
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
export PATH=/home/kalina/.local/bin:$PATH
```

Dla **Windowsa** jest ładnie opisana instalacja:  
[https://github.com/pdm-project/pdm](https://github.com/pdm-project/pdm)

* * *

**STWORZENIE PROJEKTU**
-----------------------

Inicjalizuje pusty projekt - większość rzeczy możesz wy-enterować na defaultowe opcje. To i tak można potem łatwo zmienić.

```text-plain
pdm init
```

Później piszesz jakieś tam kody w katalogu **src**. Aby je odpalić musisz kolejno:

```text-plain
pdm sync                      -> instaluje paczi zapisane w pliku lock
pdm update                    -> zaktualizuje plik lock i nastepnie wykona pdm sync
pdm install                   -> znajdzie zmiany w pliku projektu, zaktualizuje plik lock i wykona pdm sync
pdm sync --clean              -> usunie paczki ktorych nie ma w pliku lock
pdm list --tree               -> wypisze drzewo zaleznosci
pdm remove nazwa_paczki       -> usunie dana paczke z pliku projektu i naszej biblioteki
pdm run python -m project			-> to uruchomi ogólnie projekt, "od maina"
pdm run python -m project.something	-> to uruchomi konkretny plik z projektu, w tym wypadku plik "something"
```

**pdm.lock**
------------

Plik na podstawie którego pdm instaju paczki. Są w nim:
* wszystkie paczki i ich wersje
* hashe paczek
* zaleznosci dla kazdej paczki
