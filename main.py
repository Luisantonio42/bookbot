from stats import *
import sys

def main():
    print(len(sys.argv))
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at: {sys.argv[1]}")

        words = count_words_from_text(sys.argv[1])
        print("----------- Word Count ----------")
        print(f"{words} words found in the document!")

        ordered_chars = sort_chars_dictionary(count_characters_from_text(sys.argv[1]))
        print("--------- Character Count -------")
        for char in ordered_chars:
            x = char["char"]
            y = char["num"]
            if x.isalpha():
                print(f"'{x}': {y}")

        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")


main()
