while True:
    number = int(input('Number == '))
    if number == 0:
        break
    while True:
        print(number)
        number -= 1
        if number < 0:
            break