x = 10
y = 20
hello_world = None
# тут ми додаємо два числа і виводимо результат додавання на екран
print(x + y)

# None -> пустий тип
hello_world = 'hello world'
# Числа int, float -> int -> цілі числа(10, 12, 219, 43242), float -> дробові числа(10.1, 23.264, 9.7)
# bool -> y > x , True or False
# str -> рядки(текст)

hello_string = 'Hello'
print(hello_string)
world_string = 'World!'
s = 'Hello World!'
# Основна операція над рядками -> об'єднання рядків(конкатенація)
result = hello_string + ' ' + world_string
print(result)
name = 'Eduard'
hello_string = f'Hi, {name}' # Hi, Eduard
print(hello_string)
hello_string = f'Hi, {name}' # Hi, name
print(hello_string)

print('didn\'t')  # didn't  \' -> апостроф а не закриття рядку
# 1 спосіб створити змінну і надати значення bool
a = True
b = False
# 2 спосіб створити змінну і надати значення bool
age = 18
adult1 = age >= 18  # True
print(adult1)
age = 15
adult2 = age >= 18  # False
print(adult2)

# > < >= <= == !=
a = 5
b = 7
c = a < b  # True
d = a > b  # False
f = a == b  # False
h = a != b  # True
print(c, d, f, h)
print('hello')

a = input('Рядок запрошення: ')
print(type(a))  # type(a) -> class 'str'
age = input('Напишіть ваш вік: ')  # '18'(str) -> 18(int)
print(int(age) >= 18)
height = input('Напишіть ваш зріст: ')  # 1.86
print(float(height) >= 1.75)

age = input('Скільки тобі років?: ') # '18'

if int(age) >= 18:  # int(age) -> '18' -> 18
    print('Ти вже повнолітній')
else:
    print('Ти ще не повнолітній')
