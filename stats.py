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
    text = get_book_text(book)
    chars_dict = {}
    # text_list = []
    for char in text:
        char.lower()
        if char not in chars_dict:
            chars_dict[char] = 1
        # text_list.append(char.lower())
        else:
            chars_dict[char] += 1
    # print(chars_dict)
    return chars_dict
