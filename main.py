def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return f"{num_words} words found in the document"

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    num_words = number_of_words(text)
    print(num_words)
main()