from stats import count_words_from_text

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    words = count_words_from_text(
        get_book_text(
            "/Users/luisgarcia/Documents/Projects/coding_exercises/backend_dev/c4_bookbot/bookbot/books/frankenstein.txt"
        )
    )
    
    print(words)


main()
