def read_contents(file_contents):
    print(f"{file_contents}")


def count_words(file_contents):
    words = file_contents.split()
    return len(words)


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
    return dict_list


def print_report(name, file_contents):
    dict_list = count_characters(file_contents)
    word_count = count_words(file_contents)
    print(f"--- Begin report of books/{name} ---")
    print(f"{word_count} words found in the document\n")
    for i in dict_list:
        print(f"The {i["char"]} character was found {i["num"]} times")
    print("--- End report ---")


def main():
    name = "frankenstein.txt"
    with open(f"books/{name}") as f:
        file_contents = f.read()
    print_report(name, file_contents)


main()
