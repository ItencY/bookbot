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

def sort_on(dict_chars):
    return dict_chars["num"]

def sorted_dict(dict_chars):
    empty_list = []
    for char in dict_chars:
        count = dict_chars[char]
        empty_list.append({"char": char, "num": count})
    empty_list.sort(reverse=True, key=sort_on)
    return empty_list