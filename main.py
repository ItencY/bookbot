from stats import get_number_of_words
from stats import get_count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def main():
    path_book = "books/frankenstein.txt"
    book_text = get_book_text(path_book)
    count_words = get_number_of_words(book_text)
    chars_dict = get_count_characters(book_text)
    print(f"{count_words} words found in the document")
    print(chars_dict)
main()