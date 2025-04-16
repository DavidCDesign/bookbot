from stats import get_book_text
from stats import get_num_words
from stats import get_num_letters
from stats import report
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    report(path_to_file)

main()