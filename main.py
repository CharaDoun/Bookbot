def main():
    with open("books/frankenstein.txt") as frankenstein:
        book_contents = frankenstein.read()
        count_words(book_contents)


def count_words(text):
    words = text.split()
    print(len(words))


main()