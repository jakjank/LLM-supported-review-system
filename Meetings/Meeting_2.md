**Plan na to spotkanie:**

*   Najlepsza forma kontaktu dla każdego z nas - mail? telefon? sms? Teams?   
    \---→ **Mail, Asana** 
*   User Stories - przejście krok po kroku, jak miałby być użyty nasz program - na podstawie tego określimy wymagania dla naszego projektu i co dokładnie ma w sobie zawierać.  
    \-----→ **Ma być automatyczne. Ktoś wstawia Pull Requesta i aplikacja sama go czyta, wrzuca do LLM i wstawia komentarz. Potencjalnie blokuje merge'owanie.** 
*   Wymagania funkcjonalne
    *   W jakim języku/w jakich językach piszemy?   
        \-----→ **Python + jeśli coś by było potrzebne – tox, nox, pdm? Najlepiej paczka Pythonowa.** 
    *   Czy tylko dla githuba?   
        \-----→ **TAK** 
    *   Windows, Linux czy oba?   
        \-----→ **Linux, ale jeśli będzie na oba, to też git. Zazwyczaj robi się obraz na jakimś Docerze i jest to Linux. Taki Job na CI, ale niech też działa lokalnie.** 
*   Jak stwierdzimy, że coś osiągnęliśmy? - Zdefiniujmy kolejne etapy otrzymywania “działającego” programu.   
    Jakie cele po kolei chcemy osiągnąć - jakie funkcjonalności będziemy wprowadzać i w jakiej kolejności?  
    \-----→  
    **MVP: Jeden projekt na którym działa cały system**  
    Pull Request, odpala się aplikacja, analizuje zmiany w kodzie, jest jeden prompt który definiuje czego oczekujemy od LLMa (to może być sztuczna zmiana, chcemy tylko sprawdzić czy działa np. zmiana wielkości liter), zamieszcza zaproponowaną zmianę w komentarzu.  
      
    **Kolejny krok: Wyszukanie konkretnego problemu, z którym ludzie sobie nie radzą i linkery statytycznie analizujące kod,**  
    Dodajemy rozwiązywanie tego problemu jako kolejny prompt (plug-in) do systemu.

**Co za tydzień?**

*   Dodać M.T. do repozytorium. **\[Jankes\]**  
     
*   Czym jest pdm i jak z nim pracować? **\[All\]**  
    [https://github.com/pdm-project/pdm](https://github.com/pdm-project/pdm)   
     
*   Czym jest PyTest/UnitTest i jak z nim pracować?  **\[Emi\]**  
     
*   Stworzenie pustego projektu w Pythonie z użyciem pdma. **\[Kalina\]**  
     
*   Dodanie skryptów Emilki do projektu z Pythona - niech stanie się z tego paczka. **\[Kalina\]**  
     
*   Dodać prosty test w PyTeście - nie musi nic ciekawego testować, może choćby dodawać dwie liczby ze sobą.  **\[Emi\]**  
    Chcemy, żeby to była jedna komenda - odpala się system i puszcza testy.  
     
*   Zarejestrować GitHub App. **\[Jankes\]**