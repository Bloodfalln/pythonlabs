
import modul2
import math


def calculate_z():
    try:
        # Зчитуємо значення n та m від користувача
        n = float(input("Введіть значення n: "))
        m = float(input("Введіть значення m: "))

        if n <= 0 or m == 0:
            print("Значення n має бути додатнім числом, а m не може дорівнювати нулю.")
        else:
            # Обчислюємо змінну z
            z = (math.sqrt(2) - math.sqrt(3 * n)) / (2 * m)

            # Виводимо результат
            print("Значення z:", z)
    except ValueError:
        print("Некоректний ввід. Введіть дійсні числа для n та m.")


# Викликаємо функцію
calculate_z()

modul2.guess_number_game()
