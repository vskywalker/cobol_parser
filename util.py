from python_cobol import python_cobol as cobol

def parse_book(book_path):
    with open(book_path, "r") as f:
        parsed_book = cobol.process_cobol(f.readlines())
    return parsed_book

def parse_line(book, line, delimiter: str):
    parsed_line = []
    start_index = 0
    end_index = 0
    for field in book:
        field_length = field.get("pic_info").get("length")
        end_index += field_length
        parsed_line.append(line[start_index:end_index])
        start_index += field_length
    return delimiter.join(parsed_line)

def parse_file(book, file_path, delimiter):
    parsed_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        parsed_lines.append(parse_line(book, line, delimiter))
    return parsed_lines

def save_csv(parsed_file, parsed_path):
    with open(parsed_path, "w") as f:
        f.writelines(parsed_file)
    return 0