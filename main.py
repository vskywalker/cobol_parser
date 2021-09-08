import os
import util

books_dir = "books"
files_dir = "files"
parsed_dir = "parsed"
delimiter = ";"

# create dirs if not exists
try: 
    os.mkdir(books_dir) 
except: 
    pass
try: 
    os.mkdir(files_dir) 
except: 
    pass
try: 
    os.mkdir(parsed_dir) 
except: 
    pass


if __name__ == "__main__":
    books_names = os.listdir(books_dir)

    for name in books_names:
        book_path = f"{books_dir}/{name}"
        file_path = f"{files_dir}/{name}".replace(".cbl", ".")
        parsed_path = f"{files_dir}/{name}".replace(".cbl", ".csv")

        parsed_book = util.parse_book(book_path)
        parsed_file = util.parse_file(parsed_book, file_path, delimiter)
        util.save_csv(parsed_file, parsed_path)