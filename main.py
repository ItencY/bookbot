def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(book_path, get_num_words(text), get_char_text(text))

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_text(text):
    chars = {}
    charlist = []
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    for c in chars:
        charlist.append({"char": c, "count": chars[c]})
    charlist.sort(reverse=True, key=sort_on)
    return charlist

def get_book_text(path):
    with open(path) as f:
        return f.read()



def sort_on(dict):
    return dict["count"]



def print_report(book, words, chars):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    for char in chars:
        print(f"The '{char['char']}' character was found {char['count']} times")
    print("--- End of report ---")


main()