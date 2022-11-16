from Task8.Resolve_Task8 import Spellchecking
import json

def get_file_data(file_directory: str):
    file = open(file_directory, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    return file_data


words = Spellchecking.split_text(get_file_data("text.txt"))

dict = {}

for word in words:
    if dict.get(word):
        dict.update({word : dict.get(word) + 1})
    else:
        dict.update({word : 1})

print(dict)