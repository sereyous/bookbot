import sys
from stats import get_num_words, get_char_count, get_sorted_char_list

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    border = "============"
    section_border = "-----------"

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_list = get_sorted_char_list(char_count)

    print(f"{border} BOOKBOT {border}\n")
    print(f"Analyzing book found at {book_path}...\n")

    print(f"{section_border} Word Count {section_border}\n")
    print(f"Found {num_words} total words\n")

    print(f"{section_border} Character Count {section_border}\n")
    for el in sorted_char_list:
        ch = el["char"]

        if not ch.isalpha():
            continue

        count = el["count"]
        print(f"{ch}: {count}\n")


main()

