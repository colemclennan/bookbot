import sys
from stats import get_num_words
from stats import char_counter
from stats import get_sorted_chars

def get_book_text(filepath):
    file_string = ''
    with open(filepath) as f:
        file_string = f.read()
    return file_string

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_string = get_book_text(sys.argv[1])
    word_count = get_num_words(book_string)
    char_count = char_counter(book_string)
    sorted_chars = get_sorted_chars(char_count)

    # print(f'{word_count} words found in the document')
    # print(char_count)
    # print(sorted_chars)
    print("======== BOOKBOT ========")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("-------- Word Count --------")
    print(f"Found {word_count} total words")
    print('-------- Character Count --------')
    for dict in sorted_chars:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("=========== END ============")

main()