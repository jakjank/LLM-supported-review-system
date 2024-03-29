# Informacje o LLM używanym:

Używamy jednego z: llama2 (https://ollama.com/library/llama2?fbclid=IwAR3V2SH5zj9JlyegSQcv7M-Nz3pbdOG4nsBw9NzeyJ9QS4J8JqY807oPLSM), 
wizard vicuna 13B (<!-- jeszcze trzeba dodac link odpowiedni -->)

## LLama2:

### Instalacja:

#### Windows:

1. pobranie ze strony (https://ollama.com/download)
2. przekonaj antywirusa, że komputer nie umrze jak się zainstalluje ollama (jest przekonany, że to przecież wirus) 
3. jak juz sie uda odpal apke (! nie widać, że jest uruchomiona!)
4. jesli nie dziala Ci 'import requests' w pythonie: poodaj się i spróbuj na czymś, na czym działa

potrzebne:
python
pip (https://phoenixnap.com/kb/install-pip-windows)

#### Linux:

1. Pobranie curl
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
2. jeśli pokazuje, że curl niezainstalowany to np:
```bash
sudo apt install curl
```
3. jeśli już jest zaistalowana ollama to będzie pobrany odpowiedni model podczas pierwszego usuchomienia, można to zrobić używając
```bash
ollama run llama2
```
4. przy okazji od razu zostanie uruchomiony czat, gdzie można porozmawiać z tym LLM-em

### Uruchamianie:
1. żeby uruchomić server należy uruchomić aplikację (Windows) lub w terminalu wpisać `ollama serve` (Linux)
2. następnie należy utuchomić program
```bash
python3 test_llama.py
```
3. Kod działa tak, że zapytanie jest wyświetlane całe na raz (kod na postawie przykładowego kodu do uruchamiania ollamy ze strony ollama.com <!-- chyba, trzeba sprawdzic -->)
