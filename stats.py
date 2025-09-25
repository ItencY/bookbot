def get_num_words(text):
    split_words = text.split()
    return len(split_words)

def get_count_char(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts