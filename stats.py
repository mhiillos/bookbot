def count_words(input):
    return len(input.split())


def count_characters(input):
    char_dict = {}
    for c in input.lower():
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return char_dict


def parse_character_dict(char_dict):
    def sort_on(dict):
        return dict["count"]

    res = []
    for k, v in char_dict.items():
        res.append({"character": k, "count": v})
    res.sort(reverse=True, key=sort_on)
    return res
