def read_contents(file_contents):
    print(f"{file_contents}")


def count_words(file_contents):
    words = file_contents.split()
    print(f"{len(words)}")


def sort_on(dict):
    return dict["num"]


def count_characters(file_contents):
    lower_string = file_contents.lower()
    chars_dict = {}

    for char in lower_string:
        if char in chars_dict and char.isalpha():
            chars_dict[char] = chars_dict[char] + 1
        elif char.isalpha():
            chars_dict[char] = 1

    dict_list = []

    for name in chars_dict:
        dict_list.append({"char": name, "num": chars_dict[name]})

    dict_list.sort(reverse=True, key=sort_on)
    print(dict_list)


def main():
    name = "frankenstein.txt"
    with open(f"books/{name}") as f:
        file_contents = f.read()
    count_words(file_contents)
    count_characters(file_contents)


main()
