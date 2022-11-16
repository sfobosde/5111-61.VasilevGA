# Spellchecking

import re

def split_text(text: str, expression = r'\b(\w+)\b'):
    words = re.findall(expression, text)
    return words

def get_neighbour_dublicates_count(text:str, word: str):
    return re.findall(f'{word} {word}', text, flags=re.IGNORECASE)

def remove_dublicates(text):
    words = split_text(text)

    for word in words:
        while get_neighbour_dublicates_count(text, word):
            text = re.sub(f'{word} {word}',
                   word,
                   text,
                   flags=re.IGNORECASE)

    return text

text = 'in comparison comparison, to dogs, cats Cats have have not undergone major changes during the domestication process.'
print(split_text(text))

print(text)
print(remove_dublicates(text))
