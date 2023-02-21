nice = True
s = 'nice' if nice else 'not nice'


if nice:
    s = 'nice'
else:
    s = 'not nice'

some_data = 'Дані' # False
message = some_data or 'Не було наших даних'
print(message)

