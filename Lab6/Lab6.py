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


def find_team_place(teams_scores, team_name):
    sorted_teams = sorted(teams_scores.items(),
                          key=lambda x: x[1], reverse=True)

    for i, (team, score) in enumerate(sorted_teams, start=1):
        if team == team_name:
            place = i
            break

    lower_teams = [team for team, score in sorted_teams[i:]]

    return place, lower_teams


teams_scores = {
    'Команда1': 30,
    'Команда2': 25,
    'Команда3': 22,
    'Команда4': 18,
    'Команда5': 16,
    'Команда6': 15,
    'Команда7': 12,
    'Команда8': 10,
    'Команда9': 8
}

while True:
    print("\nМеню операцій:")
    print("1. Вивести всі значення словника")
    print("2. Додати або оновити запис у словнику")
    print("3. Видалити запис зі словника")
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
        if team_name in teams_scores:
            place, lower_teams = find_team_place(teams_scores, team_name)
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
