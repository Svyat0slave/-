def додавання(x, y):
    return x + y

def віднімання(x, y):
    return x - y

def множення(x, y):
    return x * y

def ділення(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    else:
        return x / y

while True:
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вийти")

    вибір = input("Введіть номер операції (1/2/3/4): ")

    if вибір == '5':
        print("Дякую за використання калькулятора. До побачення!")
        break

    число1 = float(input("Введіть перше число: "))
    число2 = float(input("Введіть друге число: "))

    if вибір == '1':
        print(число1, "+", число2, "=", додавання(число1, число2))

    elif вибір == '2':
        print(число1, "-", число2, "=", віднімання(число1, число2))

    elif вибір == '3':
        print(число1, "*", число2, "=", множення(число1, число2))

    elif вибір == '4':
        print(число1, "/", число2, "=", ділення(число1, число2))

    else:
        print("Некоректний ввід")
