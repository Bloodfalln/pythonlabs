def insert_after(lst, value, new):
    try:
        idx = lst.index(value)
        lst.insert(idx + 1, new)
        return lst
    except ValueError:
        print(f"Елемент '{value}' не знайдено у списку.")
        return lst


# Заданий список
lst = ['1', '2', 'cat', '22', 'Kyiv', '23', '442', 'pain', '1.5']
print(lst)

# Користувач вводить значення value та new_element
value = input("Введіть значення, після якого слід вставити новий елемент: ")
new_element = input("Введіть новий елемент, який слід вставити: ")

result_lst = insert_after(lst, value, new_element)
print("Оновлений список:", result_lst)
