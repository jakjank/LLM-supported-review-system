**TO DO**
---------

*   Znaleźć toole do łatwego puszczania testów - jakiś skrypt or sth. PDM to powinien mieć. Chcemy odpalać testy jedną komendą, jakimś <pdm run tests>   
     
*   Znaleźć tool do automatycznego aktualizowania wersji aplikacji.   
     
*   Rozbić kod test\_llama.py w logiczny sposób → testy mają być w testach, funkcje pozostałe w source.   
     
*   Wpisać wersje requesta i pytesta i wszystkich bibliotek, z których korzysta nasz kod, do .toml. Stworzyć na podstawie tego .lock i scommitować dla wszystkich.   
     
*   Uruchomić “jakiegoś CI” dla tego projektu.
    *   Poczytać o CI.
    *   Uruchomić owego CI.   
         
*   Poczytać więcej o webhookach. 

* * *

**ORGANIZACJA PRACY NA GITHUBIE**
---------------------------------

**Commity niech mają swój schemat opisu:**  
[https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)  

Forma:

&nbsp; &nbsp; commit -m “type\[optional scope\]: \[Asana-0000\] description”

Gdzie:

&nbsp; &nbsp; type

&nbsp; &nbsp; &nbsp; &nbsp; fix = patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).

&nbsp; &nbsp; &nbsp; &nbsp; feat = introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).

&nbsp; &nbsp; &nbsp; &nbsp; feat!/chore! = introduces a breaking API change (correlating with MAJOR in Semantic Versioning).

&nbsp; &nbsp; &nbsp; &nbsp; chore = updating grunt tasks etc; no production code change

&nbsp; &nbsp; optional scope

&nbsp; &nbsp; &nbsp; &nbsp; Zakres/dziedzina, której dotyczy commit.

&nbsp; &nbsp; Asana-0000

&nbsp; &nbsp; &nbsp; &nbsp; Zamiast 0000 napisz numer zadania z Asany. Dla zadania 17 byłoby to: Asana-0017.

Przykłady:

&nbsp; &nbsp; feat(lang): \[Asana-0017\] add Polish language

&nbsp; &nbsp; feat(api)!: \[Asana-0126\] send an email to the customer when a product is shipped

&nbsp; &nbsp; chore!: \[Asana-0001\] drop support for Node 6

&nbsp; &nbsp; fix: \[Asana-3452\] prevent racing of requests

**Konwencja zapisu wersji:**  
[https://en.wikipedia.org/wiki/Software\_versioning](https://en.wikipedia.org/wiki/Software_versioning) 

Semantic Versioning is a 3-component number in the format of X.Y.Z, where :  

*   **X** stands for a **major version**. The leftmost number denotes a major version. When you increase the major version number, you increase it by one but you reset both patch version and minor versions to zero. If the current version is 2.6.9 then the next upgrade for a major version will be 3.0.0. Increase the value of X when breaking the existing API.
*   **Y** stands for a **minor version**. It is used for the release of new functionality in the system. When you increase the minor version, you increase it by one but you must reset the patch version to zero. If the current version is 2.6.9 then the next upgrade for a minor version will be 2.7.0. Increase the value of Y when implementing new features in a backward-compatible way.
*   **Z** stands for a **Patch Versions:** Versions for patches are used for bug fixes. There are no functionality changes in the patch version upgrades. If the current version is 2.6.9 then the next version for a patch upgrade will be 2.6.10. There is no limit to these numbers. Increase the value of Z when fixing bugs

**Wrzucamy przez branche!**

*   Branch niech się nazywa jak task z Asany.   
    <git checkout -b “nazwa\_brancha”>
*   Żeby sobie pobrać, co się w międzyczasie zmieniło w main:   
    <git pull --rebase origin main>
*   Tworzymy Pull Requesta i M.T. dodaje komentarz.   
    <git push --force-with-lease origin nazwa\_brancha>
