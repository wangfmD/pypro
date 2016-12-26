def break_words(stuff):
    words = stuff.split(' ')
    return words

# print break_words("I am wfm")


def sort_word(ol):
    return sorted(ol)

# print sort_word('cba dd aa ')


def print_first_word(ik):
    print ik.pop(0)

a = ["word", "hellow"]
# a = {"c": "1", "b": "2"}
# print_first_word(a)


def print_last_word(ik):
    ik = ik.pop(-1)
    return ik
