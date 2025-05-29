from stats import number_of_words
from stats import get_count_character

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    num_words = number_of_words(text)
    print(num_words)
    count_char = get_count_character(text)
    print(count_char)
main()