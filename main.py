def main():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count()} words found in the document\n")

    char_list = how_many_chars()
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


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
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)  # sorts in descending order
    return char_list  # returns the sorted list

def sort_on(dict):
    return dict["num"]





if __name__ == "__main__":
    main()