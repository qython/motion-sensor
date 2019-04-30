# motion-sensor

## Setup

1. Zainstaluj **Pythona** (wersja 3).
```bash
user@host:~$ apt install python3 -y
```

2. Zainstaluj **cmake**.
```bash
user@host:~$ apt install cmake -y
```

3. Zainstaluj **virtualenv**.
```bash
user@host:~$ python3 -m pip install virtualenv
```

3. Będąc w katalogu głownym projektu utwórz środowisko wirtualne (np. 'env')
```bash
user@host:~/projects/motion-sensor$ python3 -m pip virtualenv .
```

Przydatne komendy:
- uruchomienie venva: 
```bash
user@host:~/projects/motion-sensor$ source /env/bin/activate
```
- wyjście ze srodowiska:
```bash
(env) user@host:~/projects/motion-sensor$ deactivate
```

- instalacja zalenżności:
```bash
(env) user@host:~/projects/motion-sensor$ python3 -m pip install -r requirements.txt
```

- zapisywanie zainstalowanych zaleznosci w srodowisku:
```bash
(env) user@host:~/projects/motion-sensor$ pip freeze > requirements.txt**
```


# Testy
Framework do testów jednostkowych: **pytest**

- Aby wykonać wszystkie testy:
```bash 
(env) user@host:~/projects/motion-sensor$ python3 -m pytest test
```

- Aby wykonać testy w podanej klasie:
```bash
(env) user@host:~/projects/motion-sensor$ python3 -m pytest test_file.py
```

- Jeśli wywołanie będzie w innym folderze niż głowny folder repozytorium to pliki mogą zostać nie odnalezione.
- Wszystkie testy są w folderze 'test'.
- Kazdy plik z testami musi posiadać prefix 'test_' - tak jak kazda fukcja która jest testem.

