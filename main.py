from stats import *

f_file = "/Users/luisgarcia/Documents/Projects/coding_exercises/backend_dev/c4_bookbot/bookbot/books/frankenstein.txt"


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {f_file}")

    words = count_words_from_text(f_file)
    print("----------- Word Count ----------")
    print(f"{words} words found in the document!")

    ordered_chars = sort_chars_dictionary(count_characters_from_text(f_file))
    print("--------- Character Count -------")
    for char in ordered_chars:
        x = char["char"]
        y = char["num"]
        if x.isalpha():
            print(f"'{x}': {y}")

    print("============= END ===============")


main()
