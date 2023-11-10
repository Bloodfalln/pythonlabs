import json
import os

teams_scores_filename = 'teams_scores.json'

# Перевірка, чи існує файл teams_scores.json
if not os.path.exists(teams_scores_filename):
    initial_data = {
        "Команда1": 30,
        "Команда2": 25,
        "Команда3": 22,
        "Команда4": 18,
        "Команда5": 16,
        "Команда6": 15,
        "Команда7": 12,
        "Команда8": 10,
        "Команда9": 8
    }
    with open(teams_scores_filename, 'w') as json_file:
        json.dump(initial_data, json_file, indent=2)


def display_dict_values(teams_scores):
    for team, score in teams_scores.items():
        print(f"{team}: {score}")


def add_or_update_entry(teams_scores, team_name, score):
    teams_scores[team_name] = score


def remove_entry(teams_scores, team_name):
    if team_name in teams_scores:
        del teams_scores[team_name]
        print(f"Запис для команди '{team_name}' видалено.")
    else:
        print(f"Команда з назвою '{team_name}' не існує в словнику.")


def display_sorted_dict(teams_scores):
    sorted_teams = sorted(teams_scores.items(),
                          key=lambda x: x[1], reverse=True)
    sorted_keys = [team for team, score in sorted_teams]
    sorted_scores = [score for team, score in sorted_teams]

    print("\nВміст словника за відсортованими ключами (за кількістю очок):")
    for i, (team, score) in enumerate(sorted_teams, start=1):
        print(f"{i}. {team}: {score}")


def find_team_place_and_save(teams_scores, team_name, output_filename):
    sorted_teams = sorted(teams_scores.items(),
                          key=lambda x: x[1], reverse=True)

    for i, (team, score) in enumerate(sorted_teams, start=1):
        if team == team_name:
            place = i
            break

    lower_teams = [team for team, score in sorted_teams[i:]]

    result_data = {
        'place': place,
        'lower_teams': lower_teams
    }

    # Зберегти результат у вказаний JSON файл
    with open(output_filename, 'w') as result_file:
        json.dump(result_data, result_file, indent=2)

    return place, lower_teams


def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(result_data, result_file, indent=2, ensure_ascii=False)


def load_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return None
    except json.JSONDecodeError:
        print(f"Помилка: Помилка декодування JSON у файлі {filename}.")
        return None


teams_scores_filename = 'teams_scores.json'
teams_scores = load_from_json(teams_scores_filename) or {}

while True:
    print("\nМеню операцій:")
    print("1. Вивести всі значення JSON файлу")
    print("2. Додати або оновити запис у JSON файлі")
    print("3. Видалити запис зі JSON файлу")
    print("4. Вивести вміст словника за кількістю очок (відсортовано)")
    print("5. Знайти місце команди та команди з меншою кількістю очок")
    print("6. Вийти з програми")

    choice = input("Виберіть операцію (1/2/3/4/5/6): ")

    if choice == '1':
        print("\nВсі значення словника:")
        display_dict_values(teams_scores)
    elif choice == '2':
        team_name = input("Введіть назву команди: ")
        score = int(input("Введіть кількість очок: "))
        add_or_update_entry(teams_scores, team_name, score)
        print(f"Запис для команди '{team_name}' додано/оновлено.")
    elif choice == '3':
        team_name = input("Введіть назву команди для видалення: ")
        remove_entry(teams_scores, team_name)
    elif choice == '4':
        display_sorted_dict(teams_scores)
    elif choice == '5':
        team_name = input("Введіть назву команди: ")
        output_filename = input(
            "Введіть ім'я JSON файлу для збереження результатів: ")
        if team_name in teams_scores:
            place, lower_teams = find_team_place_and_save(
                teams_scores, team_name, output_filename)
            print(f"Команда '{team_name}' зайняла {
                  place}-е місце у чемпіонаті.")
            print(f"Команди, які набрали менше очок, ніж '{
                  team_name}': {', '.join(lower_teams)}")
        else:
            print(f"Команда з назвою '{team_name}' не існує в словнику.")
    elif choice == '6':
        break
    else:
        print("Некоректний вибір. Будь ласка, виберіть операцію зі списку.")
