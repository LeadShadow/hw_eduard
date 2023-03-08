# continue
a = 0

while a < 6:
    a += 1
    if not a % 2:
        continue
    print(a)

# if 10 > 5:
# True or False -> 1 or 0
# if a % 2 -> 1 -> непарні числа
# if not a % 2 -> парні (if a % 2 == 0)

# ТАК НЕ РОБИТИ!
# number = int(input('number == '))
# if number < 0:
#     break

# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

n = input('Enter a number: ')  # '100'
count_zero = 0

for i in n:  # i == '1', i == '0', i == '0'
    if i == '0':  # '1' == '0', '0' == '0', '0' == '0'
        count_zero += 1

print(count_zero)

num = input('Enter the first number: ')  # '80'
length = len(num) # 2

if length == 2 and int(num) % 2 == 0:  # '80' -> 80
    print('Парне двухзначне число')
else:
    print(f'Якесь інше число {num}')