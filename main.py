from stats import get_number_of_words
from stats import get_count_characters
from stats import sorted_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    count_words = get_number_of_words(book_text)
    chars_dict = get_count_characters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    sorted_count_char = sorted_dict(chars_dict)
    for char_entry in sorted_count_char:
        char = char_entry["char"]
        num = char_entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")
main()