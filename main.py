def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def number_of_words(book_text):
    text = get_book_text(book_text)
    words = text.split()
    count_words = len(words)
    return f"{count_words} words found in the document"

def main():
    path_book = "books/frankenstein.txt"
    print(get_book_text(path_book))
    print(number_of_words(path_book))
main()