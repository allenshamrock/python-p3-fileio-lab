def write_file(file_name, file_content):
    with open(str(file_name) + '.txt', mode='w', encoding='utf-8') as text_file:
        text_file.write(file_content)


def append_file(file_name, append_content):
    with open(str(file_name) + '.txt', mode='a', encoding='utf-8') as text_file:
        text_file.write(append_content)


def read_file(file_name):
    with open(str(file_name) + '.txt', encoding='utf-8') as text_file:
        return text_file.read()
