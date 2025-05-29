def number_of_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return f"{num_words} words found in the document"

def get_count_character(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts