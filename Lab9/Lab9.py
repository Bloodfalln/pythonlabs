try:
    # Створення файлу TF1_1
    with open("TF1_1.txt", "w") as file:
        file.write(
            "Hello, world!\nThis is a sample text with some words.\nPython programming is fun!")
    print("Файл TF1_1 успішно створено.")

    # Читання та розділення слів в TF1_1 і запис у файл TF1_2
    with open("TF1_1.txt", "r") as input_file, open("TF1_2.txt", "w") as output_file:
        for line in input_file:
            words = line.split()
            for word in words:
                # Видалення розділових знаків (можливо, вам потрібно визначити, які символи вважати розділовими)
                word = ''.join(filter(str.isalnum, word))
                output_file.write(word + "\n")
    print("Записано у файл TF1_2.")

    # Читання та виведення вмісту файлу TF1_2 по рядках
    with open("TF1_2.txt", "r") as output_file:
        print("\nВміст файлу TF1_2:")
        for line in output_file:
            print(line.strip())

except FileNotFoundError:
    print("Помилка: Файл не знайдено.")
except Exception as e:
    print(f"Помилка: {e}")
