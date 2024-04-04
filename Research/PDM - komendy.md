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
pdm install
pdm run python -m project			-> to uruchomi ogólnie projekt, "od maina"
pdm run python -m project.something	-> to uruchomi konkretny plik z projektu, w tym wypadku plik "something"
```