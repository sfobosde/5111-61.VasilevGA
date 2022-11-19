def read_file_data(file_directory):
    try:
        with open(file_directory, encoding='utf-8') as program_file:
            file_content = program_file.read()
            return file_content
    except FileNotFoundError:
        raise Exception("Cannot open file")


try:
    print(read_file_data('file.txt'))
except Exception as e:
    print(str(e))
