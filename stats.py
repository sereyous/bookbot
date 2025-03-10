def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

def sort_on(dict):
    return dict["count"]

def get_sorted_char_list(chars):
    char_list = []
    for c, cnt in chars.items():
        char_list.append({"char": c, "count": cnt})
    char_list.sort(key=sort_on, reverse=True)
    return char_list
