def clear_text(text: str) -> str:
    signs_to_delete = "()[]{},:;.'-"
    for sign in signs_to_delete:
        text = text.replace(sign, "")
    text = text.lower()
    return text


def make_split(text: str, separator: str = " ") -> list:
    return text.split(separator)


def no_of_words(list_of_words: list) -> int:
    return len(list_of_words)


def no_of_unique_elements(list_of_words: list) -> int:
    return len(set(list_of_words))


def reps_of_words(list_of_words: list) -> list:
    reps = {}
    for word in list_of_words:
        if word in reps.keys():
            reps[word] += 1
        else:
            reps[word] = 1
    reps = sorted(reps.items(), key=lambda x: x[1], reverse=True)
    return reps
