from Task8.Resolve_Task8 import Spellchecking
import json


def get_file_data(file_directory: str):
    file = open(file_directory, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    return file_data


words = Spellchecking.split_text(get_file_data("text.txt"))
words_dict = {}

for word in words:
    if words_dict.get(word):
        words_dict.update({word: words_dict.get(word) + 1})
    else:
        words_dict.update({word: 1})

print(words_dict)

dict_json = json.dumps(words_dict)

with open('text_json.txt', 'w') as json_text_file:
    json_text_file.write(dict_json)
