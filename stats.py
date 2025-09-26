def get_num_words(text):
    split_words = text.split()
    return len(split_words)

def get_chars_dict(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list