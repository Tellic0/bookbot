def read_contents(file_contents):
    print(f"{file_contents}")


def count_words(file_contents):
    words = file_contents.split()
    print(f"{len(words)}")


def main():
    name = "frankenstein.txt"
    with open(f"books/{name}") as f:
        file_contents = f.read()
    read_contents(file_contents)
    count_words(file_contents)


main()
