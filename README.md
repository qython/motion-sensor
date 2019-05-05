# motion-sensor

# Michałowice
=======

## Setup

1. Zainstaluj Pythona w wersji przynajmniej 3.7.
2. Zainstaluj **virtualenv** ( **pip install virtualenv** lub **python -m pip install virtualenv**).
3. Utwórz wiertualne środowisko (venv) za pomocą **virtualenv .** lub **python -m virtualenv .** - upewnij sie ze jestes w katalogu głównym.

Uruchomienie venva: **source bin/activate**
Wyjście z venva: **deactivate**
Instalacja zalenznosci: **pip install -r requirements.txt**

Na kazdym systemie to powinno wyglądać tak samo (na Windowsie lepiej korzystać z Git Basha).

## Zapisywanie zaleznosci
**pip freeze > requirements.txt**

# Testy
Framework do testów jednostkowych: **pytest**
Wykonywanie testów: **pytest test** będąc w katalogu głównym repozytorium.

Wszystkie testy są w folderze 'test'.
Kazdy plik z testami musi posiadać prefix 'test_' - tak jak kazda fukcja która jest testem.

