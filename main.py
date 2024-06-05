def read_contents(name):
    with open(f"books/{name}") as f:
        file_contents = f.read()
    print(f"{file_contents}")


def main():
    read_contents("frankenstein.txt")


main()
