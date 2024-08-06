import random

# Случайное число от 1 до 100
secret_number = random.randint(1, 100)

# Количество попыток
guesses_left = 3

# Функция для проверки ответа
def check_answer(user_guess):
    global guesses_left
    if user_guess == secret_number:
        print("Вы угадали! Число было", secret_number)
        return True
    elif user_guess > secret_number:
        print("Ваше число слишком большое. Попробуйте еще раз.")
    elif user_guess < secret_number:
        print("Ваше число слишком маленькое. Попробуйте еще раз.")
    guesses_left -= 1
    if guesses_left == 0:
        print("Вы исчерпали все попытки. Игра окончена.")
        return False
    return False

# Основной цикл игры
while True:
    # Запрос числа у пользователя
    user_guess = int(input("Попробуйте угадать число от 1 до 100: "))
    # Проверка ответа
    if check_answer(user_guess):
        break

print("Спасибо за игру!")