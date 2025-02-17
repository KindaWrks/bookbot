def main():
    print(get_word_count())
    print(how_many_chars())


def get_word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        return word_count

def how_many_chars():
    char_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        for char in file_contents.lower():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


if __name__ == "__main__":
    main()