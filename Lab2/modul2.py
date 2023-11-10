import random


def guess_number_game():
    # Загадуємо випадкове число від 1 до 100
    random_chislo = random.randint(1, 100)

    while True:
        try:
            # Користувач вводить свій варіант
            Vvedene_chislo = int(input("Вгадайте число (від 1 до 100): "))

            if Vvedene_chislo < 1 or Vvedene_chislo > 100:
                print("Введене число не входить в діапазон від 1 до 100.")
                continue  # Перейти до наступної ітерації циклу

            if Vvedene_chislo < random_chislo:
                print("Моє число більше.")
            elif Vvedene_chislo > random_chislo:
                print("Моє число менше.")
            else:
                print("Ви вгадали!")
                break
        except ValueError:
            print("Некоректний ввід. Введіть ціле число від 1 до 100.")


# Викликаємо функцію гри
guess_number_game()
