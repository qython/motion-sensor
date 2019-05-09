# motion-sensor

#### Setup

1. Zainstaluj **pythona3**, **python3-pip**, i  **cmake** (przy użyciu dowolnego menagera paczek dla dystrybucji Linux, brew dla MacOS, lub standardowej instalacji dla Windowsa)

    Windows: [Python](https://www.python.org/downloads/) [Cmake](https://cmake.org/download/)
    
2. Zainstaluj **virtualenv**.
    ```bash
    pip3 install virtualenv
    ```
    
3. Będąc w katalogu głownym projektu utwórz środowisko wirtualne (np. 'env')
    ```bash
    virtualenv env
    ```

#### Przydatne komendy
- uruchomienie venva
    ```bash
    source /env/bin/activate
    ```
- wyjście ze srodowiska
    ```bash
    deactivate
    ```
- instalacja zalenżności
    ```bash
    pip3 install -r requirements.txt
    ```
- zapisywanie zainstalowanych zalezżości
    ```bash
    pip3 freeze > requirements.txt
    ```

# Testy
Framework do testów jednostkowych: **pytest**

1. Zainstaluj motion-sensor jako paczkę.
    ```bash 
    pip install -e .
    ```

2. Uruchom testy.
    ```bash 
    pytest tests
    ```

- Testy wykonuj zawsze będąc w głównym folderze repozytorium.
- Wszystkie testy są w folderze 'tests'.
- Kazdy plik z testami musi posiadać prefix 'test_' - tak samo jak każda fukcja która jest testem.

