def get_num_words(book_string):
    word_count = len(book_string.split())
    # print(f'{word_count} words found in the document')
    return word_count

def char_counter(book_string):
    char_count = {}
    book_by_char = list(book_string)
    for char in book_by_char:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_chars(char_count):
    sorted_char = []
    for char in char_count:
        char_info = {}
        char_info['char'] = char
        char_info['num'] = char_count[char]
        sorted_char.append(char_info)
    def getCharCount(e):
        return e['num']
    sorted_char.sort(reverse=True, key=getCharCount)

    return sorted_char