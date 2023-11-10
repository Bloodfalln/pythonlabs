def find_chars(word):
    current_char = word[0]
    current_count = 1
    max_count = 1

    for char in word[1:]:
        if char == current_char:
            current_count += 1
        else:
            current_char = char
            current_count = 1

        max_count = max(max_count, current_count)

    return max_count


word = input("Введіть слово: ")
max_count = find_chars(word)
print("Найбільша кількість однакових символів, розташованих підряд:", max_count)
