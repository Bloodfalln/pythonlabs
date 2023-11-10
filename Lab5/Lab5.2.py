# Функція для генерації послідовності чисел Фібоначчі до певної максимальної межі
def generate_fibonacci(max_limit):
    fib_sequence = [1, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= max_limit:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return set(fib_sequence)


numbers = set(range(1, 51))
print(numbers)
fibonacci = generate_fibonacci(50)

common = numbers & fibonacci

print("Кількість чисел Фібоначчі в множині: ", len(common))
print("Числа Фібоначчі в множині: ", sorted(list(common)))
