import subprocess
import locale

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление в формат Unicode и также
# проверить тип и содержимое переменных.

print("Задача 1:")
word1 = "разработка"
word2 = "сокет"
word3 = "декоратор"

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)

word1 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
word2 = "\u0441\u043e\u043a\u0435\u0442"
word3 = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)
print('\n')

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode
#  и decode) и определить тип, содержимое и длину соответствующих переменных.

print("Задача 2:")
for el in [b"class", b"function", b"method"]:
    print(type(el))
    print(el)
    print(len(el))
print('\n')

# 3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.
print("Задача 3:")
for s in ['attribute', 'класс', 'функция', 'type']:
    try:
        print(s, type(s), s.encode('ascii'), ' - успешное кодирование')
    except:
        print(s, type(s), ' - не успешное кодирование')
print('\n')

# 4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить обратное
# преобразование (используя методы encode и decode).

print("Задача 4:")
for el in ['разработка','администрирование','protocol','standard']:
    el_e = el.encode('utf-8','replace')
    el_d = el_e.decode('utf-8')
    print("Элемент: ", el)
    print("из строки в байт - ", el_e)
    print("из байт в строку - ", el_d)
print('\n')

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

print("Задача 5:")

for sites in ['yandex.ru', 'youtube.com']:
    args = ['ping', sites]
    subproc_ping = subprocess.Popen(args, stdout = subprocess.PIPE)
    for line in subproc_ping.stdout:
        print(line.decode('cp866').encode('utf-8').decode('utf-8'))
print('\n')

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку
# файла по умолчанию. Принудительно открыть файл в формате Unicode и
# вывести его содержимое.

print("Задача 6:")

print(locale.getpreferredencoding())

file = open("test_file.txt", "w")
file.write("сетевое программирование\n")
file.write("сокет\n")
file.write("декоратор\n")

file.close()

with open("test_file.txt") as f_n:
    for el_str in f_n:
        print(el_str, end='')

# Выдает ошибку при кодировании в Unicode
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
# with open("test_file.txt", encoding="utf-8") as f_n2:
#     for el_str2 in f_n2:
#         print(el_str2, end='')