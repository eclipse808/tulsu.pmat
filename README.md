# Лабораторная работа №1
1. Переходим в папку lab 1:
```
cd lab1
```
2. Необходимо сделать все файлы исполняемыми:
 ```
sudo chmod +x generate.py calculate.py sqrt.py
```
3. Запуск программы:
```
./generate.py | ./calculate.py 2> errors.txt | ./sqrt.py 2>> errors.txt
```
