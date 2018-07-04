# Завдання 1.
# Створити функцію що приймає число, перевіряє його та виводить “Even” або “Odd”

def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"
print(even_or_odd(4))