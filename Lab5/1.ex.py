import re

def match_pat(s):
    pattern = r'^ab*$'
    if re.match(pattern, s):
        return True
    else:
        return False

test_str = ['a', 'ab', 'abb', 'abbbb', 'b', 'bbb']
for test in test_str:
    print(f"{test}: {match_pat(test)}")

import re

# Открываем файл на чтение
with open("row.txt", "r") as file:
    # Читаем строки файла
    lines = file.readlines()

    # Используем регулярное выражение для поиска строк с "мл" или "фл"
    pattern = re.compile(r'\b\w*(мл|фл)\w*\b')

    # Выводим найденные строки
    for line in lines:
        if pattern.search(line):
            print(line.strip())