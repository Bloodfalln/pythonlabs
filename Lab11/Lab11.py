import csv


def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None


def search_gdp_per_capita(data, countries):
    result = []
    for row in data:
        country_name = row.get('Country Name', '')
        gdp_per_capita = row.get('2019 [YR2019]', '')

        if country_name and gdp_per_capita:
            country_name = country_name.strip()
            if any(country.lower() in country_name.lower() for country in countries):
                result.append({'Country': country_name,
                              'GDP per Capita (2019)': gdp_per_capita})

    return result


def write_csv_file(data, output_file):
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Country', 'GDP per Capita (2019)']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Результат пошуку збережено у файлі {output_file}.")
    except Exception as e:
        print(f"Помилка при збереженні результату: {e}")


if __name__ == "__main__":
    csv_file_path = 'Lab11.csv'
    output_file_path = 'new_Lab11.csv'

    # Зчитуємо дані з CSV файлу
    data = read_csv_file(csv_file_path)

    if data:
        # Користувач вводить країни для пошуку
        countries_to_search = input(
            "Введіть назви країн для пошуку (через кому): ").split(',')

        # Пошук та виведення результату на екран
        search_result = search_gdp_per_capita(data, countries_to_search)
        for row in search_result:
            print(row)

        # Збереження результату у новий CSV файл
        write_csv_file(search_result, output_file_path)
