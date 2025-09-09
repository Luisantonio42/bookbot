def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            # f is a file object
            file_contents = f.read()
            return file_contents
    except Exception as e:
        print("Please insert a valid path")


def count_words_from_text(book):
    text = get_book_text(book)
    if type(text) == str and len(text) > 0:
        return len(text.split())
    else:
        return "NaN"


def count_characters_from_text(book):
    # transform book to text
    text = get_book_text(book)
    chars_dict = {}

    # Reads every character from string
    for char in text:
        lower_char = char.lower()

        # If char not in dic add it
        if lower_char not in chars_dict:
            chars_dict[lower_char] = 1

        # else, increase count
        else:
            chars_dict[lower_char] += 1

    return chars_dict
