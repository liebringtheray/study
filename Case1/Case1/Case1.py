import math

def factorial(n):
    """Вычисляет факториал числа n."""
    if not isinstance(n, int):
        raise TypeError("Факториал может быть вычислен только для целых чисел.")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен.")
    elif n == 0 or n == 1:
        return 1
    else:
        return math.factorial(n)

# Запрашиваем число у пользователя
while True:
    try:
        number = float(input("Введите положительное целое число: "))
        if number.is_integer():  # Проверяем, является ли число целым
            number = int(number)
            break
        else:
            print("Введенное число должно быть целым.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

# Проверяем, является ли введенное число положительным целым числом
while number <= 0:
    print("Пожалуйста, введите положительное число.")
    while True:
        try:
            number = float(input("Введите число еще раз: "))
            if number.is_integer():  # Проверяем, является ли число целым
                number = int(number)
                break
            else:
                print("Введенное число должно быть целым.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

# Вычисляем и выводим факториал числа
result = factorial(number)
print(f"Факториал числа {number} равен {result}.")