def swap_words(sentence):
    # Розділяємо речення на слова
    words = sentence.split()

    # Перевіряємо, чи в реченні є принаймні два слова
    if len(words) >= 2:
        # Міняємо місцями перше та останнє слова
        words[0], words[-1] = words[-1], words[0]

        # Збираємо слова назад у речення
        modified_sentence = ' '.join(words)

        return modified_sentence
    else:
        return "Недостатньо слів у реченні для обміну."


# Користувач вводить речення
sentence = input("Введіть речення: ")

# Викликаємо функцію для міняння місцями першого та останнього слова
result = swap_words(sentence)

# Виводимо результат
print("Результат:", result)
