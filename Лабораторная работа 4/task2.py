# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    dict_list = [] #список словарей
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dict_list.append(row)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as file:
        for data in dict_list:
            json.dump(data, file, indent='    ')


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
