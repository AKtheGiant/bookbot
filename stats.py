def get_word_count(book_text):
    words = book_text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count
def character_count(book_text):
    lettercounts = dict()
    words = book_text.lower()
    for letter in words:
        if letter not in lettercounts:
            lettercounts[letter] = 1
        else:
            lettercounts[letter] += 1
    return lettercounts
def sort_on(dict):
    return dict["num"]
def letter_sort(lettercounts):
    nice_list = []
    for char, count in lettercounts.items():
        nice_list.append({"char": char, "num": count})
    nice_list.sort(reverse=True, key=sort_on)
    return nice_list

