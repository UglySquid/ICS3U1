"""
Author: Christine Wei
Date: April 21, 2023,
Description: Book class
"""


class Book(object):
    """
    Parameters: title, author, publisher
    Instance variables: title, author, publisher
    Accessor methods: get_title(), get_author(), get_publisher()
    Mutator methods: set_title(), set_author(), set_publisher()
    """
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def set_publisher(self, new_publisher):
        self.__publisher = new_publisher

    def __str__(self):
        return f"{self.__title} is written by {self.__author} and published by {self.__publisher}"


def main():
    # Create an instance of the book object
    book = Book("Tuesdays with Morie", "Mitch Albom", "Doubleday")

    # Displays info before book has changed
    print(f"""
    title: {book.get_title()}
    author: {book.get_author()}
    publisher: {book.get_publisher()}""")

    print("\n", book)

    # Changes book info
    book.set_title("Little Fires Everywhere")
    book.set_author("Celeste Ng")
    book.set_publisher("Penguin Press")

    # Displays info after book has changed
    print(f"""
    title: {book.get_title()}
    author: {book.get_author()}
    publisher: {book.get_publisher()}""")

    print("\n", book)


main()
