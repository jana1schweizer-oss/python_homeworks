import csv

# читаємо перший файл
with open('ideas_for_test/work_with_csv/random.csv', newline='', encoding='utf-8') as f1:
    reader1 = list(csv.reader(f1))

# читаємо другий файл
with open('ideas_for_test/work_with_csv/rmc.csv', newline='', encoding='utf-8') as f2:
    reader2 = list(csv.reader(f2))
# об'єднуємо два списки
combined = reader1 + reader2
# прибираємо дублікати
unique_rows = []
seen = set()

for row in combined:
    row_tuple = tuple(row)  # робимо рядок хешованим
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_rows.append(row)
# записуємо результат у файл
with open('ideas_for_test/work_with_csv/result_schweizer.csv', 'w', newline='', encoding='utf-8') as result_file:
    writer = csv.writer(result_file)
    writer.writerows(unique_rows)
import json
import logging
import os

# налаштовуємо логер
logging.basicConfig(
    filename='ideas_for_test/work_with_json/json_schweizer.log',  # заміни smirnova на свою фамілію
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# шлях до папки з JSON
json_folder = 'ideas_for_test/work_with_json'

# отримуємо список файлів
json_files = os.listdir(json_folder)
# перевіряємо валідність кожного JSON-файлу
for file_name in json_files:
    file_path = os.path.join(json_folder, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)  # пробуємо прочитати JSON
    except Exception as e:
        logging.error(f'Файл {file_name} невалідний: {e}')
import xml.etree.ElementTree as ET

# читаємо XML-файл
xml_path = 'ideas_for_test/work_with_xml/groups.xml'
tree = ET.parse(xml_path)
root = tree.getroot()
# знаходимо group/number
group = root.find('group')
number = group.find('number').text
# знаходимо timingExbytes/incoming
timing = group.find('timingExbytes')
incoming = timing.find('incoming').text
# виводимо результат
logging.info(f'Group number: {number}, incoming: {incoming}')

