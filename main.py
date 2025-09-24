def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    path_to_file = "./books/frankenstein.txt"
    read_file = get_book_text(path_to_file)
    print(read_file)


main()