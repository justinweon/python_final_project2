class Book:
    def __init__(self, title, author,isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True 

    def get_title(self):
        return self.__title

    def get_isbn(self):
        return self.__isbn

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__is_available

    def rent_book(self):
        self.__is_available = False

    def return_book(self):
        self.__is_available = True

    def display_info(self):
        status = "대여가능" if self.is_available() else "대여중"
        return f"[{status}] {self.__title} / {self.__author}"
