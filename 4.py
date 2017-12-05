def is_valid(s):
    words = s.split()
    return len(set(words)) == len(words)


def is_valid2(s):
    words = s.split()
    already_in_use = [set(words[0])]
    for word in words[1:]:
        word_set = set(word)
        if word_set in already_in_use:
            return False
        already_in_use.append(word_set)
    return True


with open('4.in') as f:
    counter = sum([1 for l in f.readlines() if is_valid(l)])
    print(counter)

with open('4.in') as f:
    counter = sum([1 for l in f.readlines() if is_valid2(l)])
    print(counter)
