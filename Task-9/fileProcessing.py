from Task8.Resolve_Task8 import Spellchecking

def get_file_data(file_directory: str):
    file = open(file_directory, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    return file_data

print(Spellchecking.split_text(get_file_data("text.txt")))