def get_number_of_words(book_text):
    words = book_text.split()
    return len(words)

def get_count_characters(book_text):
    chars = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] = chars[lower_char] + 1
        else:
            chars[lower_char] = 1
    return chars