# Spellchecking

import re

# Spli text on words with regular expression.
def split_text(text: str, expression = r'\b(\w+)\b'):
    words = re.findall(expression, text)
    return words

# Check neighbour duplicates.
# Example: comparsion comparsion, comparsion Comparsion
def get_neighbour_duplicates(text:str, word: str):
    return re.findall(f'{word} {word}', text, flags=re.IGNORECASE)

# Remove word duplicates.
def remove_duplicates(text):
    # Split text on words.
    words = split_text(text)

    # Check neighbour duplicates.
    for word in words:
        # Remove duplicates while 1 word left.
        while get_neighbour_duplicates(text, word):
            text = re.sub(f'{word} {word}',
                   word,
                   text,
                   flags=re.IGNORECASE)

    return text

text = 'в сравнение сравнение сравнение Сравнение с собаками, кошками Кошки не претерпели серьезных изменений в процессе одомашнивания.'
print(text)
print(remove_duplicates(text))
