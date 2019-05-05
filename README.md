# motion-sensor

## Setup

1. Zainstaluj **Pythona** (wersja 3) i  **cmake**.
Ubuntu:
```bash
user@host:~$ apt install python3 cmake -y
```
Windows:
[Pobierz Pythona](https://www.python.org/downloads/)
[Pobierz Cmake](https://cmake.org/download/)

2. Zainstaluj **virtualenv**.
Linux
```bash
user@host:~$ python3 -m pip install virtualenv
```
Windows
```bash
C:\Projects\motion-sensor> python3 -m pip install virtualenv
```
3. Będąc w katalogu głownym projektu utwórz środowisko wirtualne (np. 'env')
Linux
```bash
user@host:~/projects/motion-sensor$ python3 -m pip virtualenv env
```
Windows
```bash
C:\Projects\motion-sensor> python3 -m pip virtualenv env
```
Przydatne komendy:
- uruchomienie venva:
Linux
```bash
user@host:~/projects/motion-sensor$ source /env/bin/activate
```
Windows
```bash
C:\Projects\motion-sensor>  /env/Scripts/activate
```
- wyjście ze srodowiska:
Linux
```bash
(env) user@host:~/projects/motion-sensor$ deactivate
```
Windows
```bash
(env) C:\Projects\motion-sensor> deactivate
```
- instalacja zalenżności:
Linux
```bash
(env) user@host:~/projects/motion-sensor$ python3 -m pip install -r requirements.txt
```
Windows
```bash
(env) C:\Projects\motion-sensor> python3 -m pip install -r requirements.txt
```
- zapisywanie zainstalowanych zaleznosci w srodowisku:
Linux
```bash
(env) user@host:~/projects/motion-sensor$ pip freeze > requirements.txt
```
Windows
```bash
(env) C:\Projects\motion-sensor> pip freeze > requirements.txt
```

# Testy
Framework do testów jednostkowych: **pytest**

- Aby wykonać wszystkie testy:
Linux
```bash 
(env) user@host:~/projects/motion-sensor$ python3 -m pytest test
```
Windows
```bash 
(env) C:\Projects\motion-sensor> python3 -m pytest test
```

- Aby wykonać testy w podanej klasie:
```bash
(env) user@host:~/projects/motion-sensor$ python3 -m pytest test_file.py
```
Windows
```bash 
(env) C:\Projects\motion-sensor> python3 -m pytest test_file.py
```

- Jeśli wywołanie będzie w innym folderze niż głowny folder repozytorium to pliki mogą zostać nie odnalezione.
- Wszystkie testy są w folderze 'test'.
- Kazdy plik z testami musi posiadać prefix 'test_' - tak jak kazda fukcja która jest testem.

