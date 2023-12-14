import pandas as pd

people_data = {
    1: {"прізвище": "Бародич", "ім'я": "Андрій", "зріст": 175, "стать": "чоловік"},
    2: {"прізвище": "Вавіло", "ім'я": "Артем", "зріст": 180, "стать": "чоловік"},
    3: {"прізвище": "Вакуленко", "ім'я": "Богдан", "зріст": 170, "стать": "чоловік"},
    4: {"прізвище": "Валюх", "ім'я": "Максим", "зріст": 165, "стать": "чоловік"},
    5: {"прізвище": "Горобець", "ім'я": "Дмитро", "зріст": 160, "стать": "чоловік"},
    6: {"прізвище": "Затварський", "ім'я": "Владислав", "зріст": 185, "стать": "чоловік"},
    7: {"прізвище": "Косілов", "ім'я": "Владислав", "зріст": 170, "стать": "чоловік"},
    8: {"прізвище": "Курас", "ім'я": "Михайло", "зріст": 178, "стать": "чоловік"},
    9: {"прізвище": "Педос", "ім'я": "Владислав", "зріст": 162, "стать": "чоловік"},
    10: {"прізвище": "Петренко", "ім'я": "Єгор", "зріст": 168, "стать": "чоловік"}
}

def display_data_as_dataframe(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    print(df)


def add_person(data, id, прізвище, ім_я, зріст, стать):
    data[id] = {"прізвище": прізвище, "ім'я": ім_я, "зріст": зріст, "стать": стать}

def delete_person(data, id):
    if id in data:
        del data[id]
        print(f"Особу з ID {id} видалено зі словника.")
    else:
        print(f"Особи з ID {id} не існує у словнику.")

def average_height_of_men(data):
        total_height = 0
        count_men = 0

        for person in data.values():
            if person["стать"] == "чоловік":
                total_height += person["зріст"]
                count_men += 1

        if count_men > 0:
            average_height = total_height / count_men
            print(f"Середній зріст чоловіків: {average_height:.2f} см")
        else:
            print("У словнику немає чоловіків.")
    # (unchanged)

def main():
    while True:
        print("\nМеню:")
        print("1. Вивести дані про всіх осіб")
        print("2. Додати нову особу")
        print("3. Видалити особу за ID")
        print("4. Розрахувати середній зріст чоловіків")
        print("5. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            display_data_as_dataframe(people_data)
        elif choice == "2":
            id = int(input("Введіть ID нової особи: "))
            прізвище = input("Введіть прізвище: ")
            ім_я = input("Введіть ім'я: ")
            зріст = int(input("Введіть зріст (у см): "))
            стать = input("Введіть стать (чоловік/жінка): ")
            add_person(people_data, id, прізвище, ім_я, зріст, стать)
        elif choice == "3":
            id = int(input("Введіть ID особи, яку потрібно видалити: "))
            delete_person(people_data, id)
        elif choice == "4":
            average_height_of_men(people_data)
        elif choice == "5":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
