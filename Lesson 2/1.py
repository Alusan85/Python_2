# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
# поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
# «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
# (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().


import csv
import re

def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []

    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']

    for file_name in file_list:
        with open(file_name, encoding='cp1251') as f_n:

            for row in f_n:
                # делим строку на ключ-значение, удобное и практичное решение
                param = re.split(":\s+", row.strip())
                # regexp \s+, режем один или больше space символов, от ":" и до текста

                if isinstance(param, list) and len(param) == 2:
                    # isinstance() специально создана для проверки принадлежности данных
                    # определенному классу (типу данных) - берем list
                    # записываем значения в массивы в соответствии с ключем

                    if param[0] == 'Изготовитель системы':
                        os_prod_list.append(param[1])
                    elif param[0] == 'Название ОС':
                        os_name_list.append(param[1])
                    elif param[0] == 'Код продукта':
                        os_code_list.append(param[1])
                    elif param[0] == 'Тип системы':
                        os_type_list.append(param[1])

    # согласно требованиям задачи, возвращать данные необходимо в виде пяти массивов:
    # заголовки, изготовитель системы, название ос, код продукта, тип системы

    header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    return header, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv():
    main_data = get_data()  # получаем данные из файла в формате, как указано в задаче
    processed_data = [main_data[0]]  # сначала заголовок
    number_of_lines = len(main_data[1])  # считаем сколько строк данных нужно записать

    for i in range(number_of_lines):
        processed_data.append([row[i] for row in main_data[1:]])  # данные построчно от заголовка и далее
    with open('result.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        for row in processed_data:
            f_n_writer.writerow(row)


if __name__ == '__main__':
    write_to_csv()
    with open('result.csv') as f_n2:
        print(f_n2.read())