def number_of_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return f"{num_words} words found in the document"