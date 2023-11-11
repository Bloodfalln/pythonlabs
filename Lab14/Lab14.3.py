import matplotlib.pyplot as plt
import numpy as np
import csv

data_saved = []
data = []

try:
    with open("Lab10.csv", "r") as file:
        reader = csv.reader(file, delimiter=',', quotechar=',')
        for row in reader:
            for elem in row:
                el = elem.replace('"', '')
                data_saved.append(el)
            data.append(data_saved)
            data_saved = []
except Exception as err:
    print(err)
    exit(0)

x = []  # роки
y1 = []  # показник для США
y2 = []  # показник для України

for num in range(2, len(data[0])):
    x.append(data[0][num])
    y1.append(round(float(data[1][num]), 5))
    y2.append(round(float(data[2][num]), 5))


def graf(x, y1, y2):
    plt.plot(x, y1, 'b', label=data[1][1],  lw=3)
    plt.plot(x, y2, 'r', label=data[2][1], lw=3)

    plt.xlabel("Рік")
    plt.ylabel("Показник")
    plt.legend()
    plt.show()


def bar(x, y1, y2):
    print("Виберіть потрібну країну:\n1 - США\n2 - Україна")
    while (True):
        ch = input("Вибір: ")
        if (ch == '1') or (ch == '2'):
            break
        else:
            print("Помилка! Спробуйте ще раз.")
    if ch == '1':
        plt.bar(x, y1, label=data[int(ch)][1])
    if ch == '2':
        plt.bar(x, y2, label=data[int(ch)][1])

    plt.xlabel("Рік")
    plt.ylabel("Показник")
    plt.legend()
    plt.show()


print("Виберіть дію:\n1 - Зображення графіка для двох країн\n"
      "2 - Зображення стовпчастої діаграми для однієї вибраної країни")
while (True):
    choice = input("Вибір: ")
    if choice == '1':
        graf(x, y1, y2)
        break
    elif choice == '2':
        bar(x, y1, y2)
        break
    else:
        print("Помилка! Спробуйте ще раз.")
