# Generate documentation file.
def generate_documentation_file(file_directory, documentation_text):
    try:
        with open(file_directory, 'w', encoding='utf-8') as program_file:
            file_content = program_file.write(documentation_text)
            return file_content
    except Exception as e:
        raise Exception(f"Cannot write or create file: {str(e)}")


# Read file content.
def read_file_data(file_directory):
    try:
        with open(file_directory, encoding='utf-8') as program_file:
            file_content = program_file.read()
            return file_content
    except FileNotFoundError as e:
        raise Exception(f"Cannot open file: {str(e)}")


try:
    file_data = read_file_data('Spellchecking.py')
    generate_documentation_file('Spellchecking.py.txt', file_data)
except Exception as e:
    print(str(e))
