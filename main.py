import sys
from stats import count_characters, count_words, parse_character_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    book_text = get_book_text(filepath)
    total_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    character_dict = count_characters(book_text)
    print("--------- Character Count -------")
    character_list = parse_character_dict(character_dict)
    for ch_dict in character_list:
        if ch_dict["character"].isalpha():
            print(f"{ch_dict['character']}: {ch_dict['count']}")
    print("============= END ===============")


main()
