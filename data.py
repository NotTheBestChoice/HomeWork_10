import pickle
import json
import yaml
from pydantic import BaseModel
from typing import Union
import pandas as pd

# Запись/чтение строки в/из файл(а):
text_file = open('test.txt', 'w', encoding='utf-8')
text_file.write('Просто строка...\n')
text_file.close()
text_file = open('test.txt', 'r', encoding='utf-8')
print(text_file.read())
text_file.close()

# Сериализация с помощью pickle
class Easy:
    def prn(txt):
        print(txt)

t = Easy

f = open('pickle.dat', 'wb')
pickle.dump(t, f)
f.close()

f = open('pickle.dat', 'rb')
t = pickle.load(f)
t.prn('Запустили метод prn после сериализации объекта...\n')
f.close()

# Объект испытаний
data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
    }

# Сериализация с помощью json
with open('json_file.json', 'w') as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)

# Десериализация с помощью json
with open('json_file.json', 'r') as read_file:
    data_from = json.load(read_file)

j_s = json.loads(json_string)

print(data_from)
print(j_s)

# Сериализация с помощью yaml
with open('yaml_file.yaml', 'w') as write_file:
    yaml.safe_dump(data, write_file)

# Десериализация с помощью yaml
with open('yaml_file.yaml', 'r') as read_file:
    data_from = yaml.safe_load(read_file)

print(data_from)
print('')

# Сериализация с помощью pydantic
class Unit(BaseModel):
    age: int
    name: str
    children: list
    married: bool
    city: Union[str,None]

print(Unit(**data))
print('')

# Таблица Excel -> csv
cnv = pd.read_excel('in_pandas.xlsx')
cnv.to_csv('out_pandas.csv', encoding='utf-8', index=False)
print('Сonversion .xslx to .csv completed successfully!')
print('')