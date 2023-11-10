# Створення двовимірного масиву
rows = 7
columns = 7
array = [[0 for _ in range(columns)] for _ in range(rows)]

# Заповнення масиву відповідно до  шаблону
for row in range(rows):
    for col in range(columns - row):
        array[row][col] = col + 1 + row

# Виведення масиву на екран
for row in array:
    for element in row:
        print(element, end='')
    print()  # Перехід на наступний рядок
