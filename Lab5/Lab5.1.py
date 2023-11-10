def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Заданий список для сортування
my_list = [3, 6, 8, 10, 1, 2, 1]
print(my_list)
# Виклик функції для швидкого сортування
sorted_list = quicksort(my_list)

# Виведення відсортованого списку
print("Відсортований список:", sorted_list)
