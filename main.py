def read_contents(name):
    with open(f"books/{name}") as f:
        file_contents = f.read()
    print(f"{file_contents}")


def count_words(name):
    with open(f"books/{name}") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(f"{len(words)}")


def main():
    read_contents("frankenstein.txt")
    count_words("frankenstein.txt")


main()
