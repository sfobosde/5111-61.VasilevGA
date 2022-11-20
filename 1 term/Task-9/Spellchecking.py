# Spellchecking

import re


# Split text on words with regular expression.
def split_text(inputted_text: str, expression=r'\b(\w+)\b'):
    words = re.findall(expression, inputted_text)
    return words


# Check neighbour duplicates.
def get_neighbour_duplicates(inputted_text: str, word: str):
    return re.findall(f'{word} {word}', inputted_text, flags=re.IGNORECASE)


# Remove word duplicates.
def remove_duplicates(inputted_text):
    # Split text on words.
    words = split_text(inputted_text)

    # Check neighbour duplicates.
    for word in words:
        # Remove duplicates while 1 word left.
        while get_neighbour_duplicates(inputted_text, word):
            inputted_text = re.sub(f'{word} {word}',
                                   word,
                                   inputted_text,
                                   flags=re.IGNORECASE)

    return inputted_text


text = 'в сравнение сравнение сравнение Сравнение с собаками, ' \
       'кошками Кошки не претерпели серьезных изменений в процессе одомашнивания.'

print(text)
print(remove_duplicates(text))
print(split_text(text))
