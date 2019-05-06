# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
# в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
# с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml

key_1 = ['Список', 'Green apple', '#$%%', '123']
key_2 = 123456789
key_3 = {
    'a': '€',
    'b': 'Æ',
}
# Подготавливаем данные для записи
data_to_yaml = {
    'key_1': key_1,
    'key_2': key_2,
    'key_3': key_3,
}
yaml_str = yaml.dump(data_to_yaml, allow_unicode=True, default_flow_style=True)
print(yaml_str)
# пишем строку в файл file.yaml
with open('file.yaml', 'w', encoding="UTF-8") as f_n:
    f_n.write(yaml_str)
# читаем из файла
with open('file.yaml', 'r', encoding="UTF-8") as f_n2:
    # немного синтетического сахара yaml.safe_load от варнингов YAMLLoadWarning
    data_from_yaml = yaml.safe_load(f_n2)
print("Read from file:\n", data_from_yaml)
# Проверяем записанное в файл и то что подготовили для записи
if data_from_yaml == data_to_yaml:
    print("It works, data the same")
else:
    print("Different data")