# and (І) -> вираз виконається, якщо обидві умови правда
# a         b      a and b
# True     True     True
# True     False    False
# False    True     False
# False    False    False

# 1 -> True,  0 -> False
# and -> операція множення
# 1 * 1 -> 1
# 1 * 0 -> 0
# 0 * 1 -> 0
# 0 * 0 -> 0

a = True and False  # False

# or (АБО) -> вираз виконається якщо хоч одне з умов виконується, тобто в одної змінної значення True
# a         b      a or b
# True     True     True
# True     False    True
# False    True     True
# False    False    False

a = True or False  # True

# not (НЕ) -> заперечення, буде обернене значення
# a      not a
# True   False
# False  True