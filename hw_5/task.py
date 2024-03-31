"""
1. Найдите информацию об организациях.
    a. Получите список ИНН из файла traders.txt.
    b. Найдите информацию об организациях с этими ИНН в файле
       traders.json.
    c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла
       traders.txt в файл traders.csv.
"""

import json
import csv

# Функция для чтения списка ИНН из файла traders.txt
def read_inn_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

# Функция для поиска информации об организациях по ИНН
def find_organizations(inn_list, json_filename):
    with open(json_filename, 'r', encoding='utf-8') as file:
        traders_data = json.load(file)
    
    organizations_info = []
    for inn in inn_list:
        for trader in traders_data:
            if 'inn' in trader and trader['inn'] == inn:
                organizations_info.append({
                    'INN': inn,
                    'OGRN': trader.get('ogrn', ''),
                    'Address': trader.get('address', '')
                })
                break  # остановиться, если найдена информация об организации
    return organizations_info

# Функция для сохранения информации об организациях в CSV файл
def save_to_csv(data, csv_filename):
    with open(csv_filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['INN', 'OGRN', 'Address'])
        writer.writeheader()
        writer.writerows(data)

# Основной код
if __name__ == "__main__":
    # Получить список ИНН из файла traders.txt
    inn_list = read_inn_from_file('/Users/artem/Desktop/HSE/Python_Lessons/hw_5/traders.txt')

    # Найти информацию об организациях с этими ИНН в файле traders.json
    organizations_info = find_organizations(inn_list, '/Users/artem/Desktop/HSE/Python_Lessons/hw_5/traders.json')

    # Сохранить информацию об ИНН, ОГРН и адресе организаций в файл traders.csv
    save_to_csv(organizations_info, '/Users/artem/Desktop/HSE/Python_Lessons/hw_5/traders.csv')
