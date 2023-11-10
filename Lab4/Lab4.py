def generate_fibonacci(n):
    if n <= 0:
        return []

    # Ініціалізуємо масив для збереження послідовності
    fibonacci = [1]

    if n > 1:
        fibonacci.append(1)

    while len(fibonacci) < n:
        next_fibonacci = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fibonacci)

    return fibonacci


while True:
    try:
        n = int(
            input("Введіть кількість чисел у послідовності Фібоначчі (додатне число): "))

        if n > 0:
            break
        else:
            print("Введіть додатне число.")
    except ValueError:
        print("Некоректний ввід. Введіть число.")

# Генеруємо послідовність Фібоначчі
fibonacci = generate_fibonacci(n)

# Виводимо результат
print("Перші", n, "чисел послідовності Фібоначчі:", fibonacci)
