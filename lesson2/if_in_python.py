money = 0

# число 0 приводиться до False -> True == 1, False == 0
if not money:  # Якщо є гроші, якщо немає то йди далі
    print('You have no money and no debts')
else: # інша умова коли немає грошей
    print(f"You have {money} on your bank account")

# None -> False
result = None
if result:  # Якщо результат правдивий, то виконуй виведення результату, якщо брехня йли далі
    print(result)
else: # інша умова, коли результат брехня
    print('Result is None')

# пустий рядок, або ж пустий контейнер приводяться до False
user_name = input("Введіть своє ім'я: ")  # ''

if user_name:
    print(f'Привіт, {user_name}')
else:
    print('Привіт, Анонім!')




