x = int(input('X: '))
y = int(input('Y: '))

if x == 0:
    print("X can't be equal to zero")
    x = int(input('X: '))
    if x == 0:
        print("X can't be equal to zero")
        x = int(input('X: '))
        if x == 0:
            print("X can't be equal to zero")
            x = int(input('X: '))
            if x == 0:
                print("X can't be equal to zero")
                x = int(input('X: '))

result = y / x


# Цикли
# Цикл for -> його називають ітеруючим, він перебирає елементи якоїсь послідовності
# apple
# Настя - а
# Саша - p
# Едуард - p
# Наташа - l
# Міша - e

fruit = 'apple'
for i in fruit:
    print(i)

# цикл починається з ключового слова for
# за яким йде обов'язково назва змінної куди буде записуватись значення, яке ми отримуємо
# з ітеруйочого об'єкту на кожній інтерації
# далі йде ключове слово in
# за яким йде вираз або об'єкт по якому ми будемо ітеруватись
# далі ставиться :
# і далі з наступного рядка з відступом йде набір виразів, які будуть повторюватись на кожній ітерації

a = 1
while a <= 5:
    print(a)
    a = a + 1  # збільши змінну a на одиничку  a = 1 + 1,  a = 2 + 1,  a = 3 + 1


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1
