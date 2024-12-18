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
# Лабораторная работа №2
1. Переходим в папку lab 2:
```
cd lab2
```
2. Необходимо сделать файл исполняем:
 ```
sudo chmod +x greeter.py
```
### Запуск программы осуществляется в двух режимах.

3. Запуск в первом режиме:
```
/greeter.py
```
Вывод программы:
```
Hey, what's your name?

Ann

Nice to see you, Ann!

Hey, what's your name?

^C
```
Для выхода из программы нажать ctr+C 

4. Запуск во втором режиме:
```
./greeter.py names.txt error.txt
```

Вывод программы:
```
Nice to see you, Nick!

Nice to see you, Kai!

Nice to see you, Tyler!
```

5. Просмотр файла с ошибками:
```
cat error.txt 
```
Вывод:
```
Ошибка: logan - недопустимое имя.

Ошибка: P33tr - недопустимое имя.

Ошибка: 321 - недопустимое имя.
```

