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


test_dict = {"t": 29493, "h": 19176, "e": 44538, " ": 70480, "p": 5952}


def sort_on(items):
    return items["num"]


def sort_chars_dictionary(chars_dictionary):
    # print(chars_dictionary)
    ordered_dicts = []
    for char in chars_dictionary:
        char_dict = {}
        char_count = chars_dictionary[char]

        char_dict["char"] = char
        char_dict["num"] = char_count

        ordered_dicts.append(char_dict)

    ordered_dicts.sort(reverse=True, key=sort_on)
    return ordered_dicts


# print(sort_chars_dictionary(test_dict))
