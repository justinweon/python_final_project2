from book import Book

class Paperbook(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title,author,isbn)
        self.pages = pages

    def display_info(self):
        base_info = super().display_info()
        return(f"{base_info}, 페이지 수: {self.pages}")



class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title,author,isbn)
        self.__file_size = file_size

    def display_info(self):
        base_info = super().display_info()
        return(f"{base_info}, 파일 크기: {self.__file_size}")