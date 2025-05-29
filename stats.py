def number_of_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return num_words

def get_count_character(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    result = [{"char": char, "num": count} for char, count in char_counts.items()]
    result.sort(key=lambda item: item["num"], reverse=True)
    return result