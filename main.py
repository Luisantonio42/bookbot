from stats import *

f_file = "/Users/luisgarcia/Documents/Projects/coding_exercises/backend_dev/c4_bookbot/bookbot/books/frankenstein.txt"

f_s_file = "/Users/luisgarcia/Documents/Projects/coding_exercises/backend_dev/c4_bookbot/bookbot/books/frank_substract.txt"


def main():
    words = count_words_from_text(f_file)

    print(f"{words} words found in the document!")

    chars_from_text = count_characters_from_text(f_s_file)

    print(chars_from_text)


main()
