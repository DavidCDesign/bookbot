def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding="utf-8") as f:
        return f.read()

def get_num_words(path_to_file):
    return len(path_to_file.split())

def get_num_letters(path_to_file):
    book_str = path_to_file.lower()

    char_list = list(book_str)
    char_set  = set(char_list)
    char_dict = {}

    for s in char_set:
        num_appearances = 0

        for l in char_list:
            if s == l:
                num_appearances += 1

        char_dict[s] = num_appearances
    return char_dict

def sort_results(text):
	character_list = []
	for char, count in text.items():
		if char.isalpha():
			character_list.append({'char': char, 'num': count})
            
	def sorter(dict):
		return dict["num"]
	character_list.sort(reverse=True, key=sorter)

	report = []
	for character in character_list:
		report.append(f"{character['char']}: {character['num']}")
	return '\n'.join(report)

def report(path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    num_letters = get_num_letters(book_text)
    sorted = sort_results(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(f"{sorted}")