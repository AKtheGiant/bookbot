import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def main():
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = get_word_count(book_text)
    characters = character_count(book_text)
    true_characters = letter_sort(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in true_characters:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
from stats import get_word_count
from stats import character_count
from stats import letter_sort
main()
