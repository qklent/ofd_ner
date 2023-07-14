#тут можно еще сделать ru_to_eng(дада и такие странные примеры есть)
def eng_to_ru(word: str) -> str:
    if len(word) <= 1:
        return word
    a = ord('а')
    ru_alphabet = ''.join([chr(i) for i in range(a,a+33)])
    eng_alphabet = string.ascii_lowercase[:26]
    change = {
        "a": "а",
        "e": "е",
        "o": "о",
        "k": "к",
        "3": "з",
        "p": "р",
        "c": "с",
        "m": "м",
        "x": "х",
        "t": "т",
        "y": "у",
        "z": "з",
    }

    new_word = ""
    for i in range(len(word)):
        curr = word[i]
        if curr in eng_alphabet:
            if i - 1 < 0:
                prev_letter = "j"
            else:
                prev_letter = word[i - 1]

            if i + 1 >= len(word):
                next_letter = "j"
            else:
                next_letter = word[i + 1]

            if next_letter in ru_alphabet or prev_letter in ru_alphabet:
                curr = change.get(curr, curr)
        new_word += curr

    return new_word

def only_ones(word: str) -> str:
    if word.isdigit() or re.match(r'^-?\d+(?:\.\d+)$', word):
        return "1"
    else:
        new_word = ""
        i = 0
        while i < len(word):
            curr = word[i]
            while i < len(word) and word[i].isdigit():
                curr = "1"
                i += 1
            new_word += curr
            if curr != "1":
                i += 1

    return new_word

def remove_punct(word: str) -> str:
    word = re.sub(r'[^\w\s]+', ' ', word)
    word = re.sub(r'\s+', ' ', word)
    return word.strip()


def preprocess_string(word: str) -> str:
    new_word = ""


    word = remove_punct(word)

    if word != "товара нет":
        new_word = eng_to_ru(only_ones(word).lower())

    return new_word
