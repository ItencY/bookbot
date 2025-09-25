from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path_to_file = "./books/frankenstein.txt"
    read_file = get_book_text(path_to_file)
    num_words = get_num_words(read_file)
    print(f"Found {num_words} total words")
main()