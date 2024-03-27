
def file_data(path):
    with open(path, "r") as file:
        data = file.read()
    return data


# Time complexity is O(n * m). n: is the total words in the text. m: is the total length for the comparison word
def count_word_first_variant(my_text, word_search):
    count = 0
    words_list = my_text.split()
    for word in words_list:
        if word_search.lower() == word.lower():
            count += 1
    return count


# Time complexity is O(n)
def count_word_second_variant(my_text, word_search):
    frequency_word_dict = {}
    my_text_list = my_text.lower().split()
    for word in my_text_list:
        frequency_word_dict[word] = frequency_word_dict.get(word, 0) + 1
    return frequency_word_dict[word_search]
