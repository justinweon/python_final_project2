from book import Book

class Library:
    def __init__(self):
        self.library : list[Book] = []

    def add_book(self, book):
        self.library.append(book)
        print(f"도서가 등록되었습니다 | {book.get_title()}")

    def display_info(self):
        if not self.library:
            print("등록된 도서가 없습니다")
        else:
            for book in self.library:
                print(book.display_info())

    def search_books(self, keyword:str):
        keyword = keyword.lower()
        results = [book for book in self.library
                  if keyword in book.get_title().lower() or keyword in book.get_author().lower()
        ]
        return results

    def borrow_books(self, isbn):
        book = self._find_by_id(isbn)
        if not book:
            print(f"{isbn} 도서를 찾을 수 없습니다.")
            return
        if book.is_available():
            book.rent_book()
            print(f"{isbn} 도서를 대여합니다.")
        else:
            print(f"{isbn} 은(는) 현재 대여중입니다.")

    def return_books(self, isbn:str):
        book = self._find_by_id(isbn)
        if not book:
            print (f"{isbn} 도서를 찾을 수 없습니다.")
            return

        if not book.is_available():
            book.return_book()
            print (f"{isbn} 도서를 반납합니다.")

        else:
            print(f"{isbn}는 대여되지 않은 도서입니다.")

    def _find_by_id(self, isbn):
        for book in self.library:
            if book.get_isbn().lower() == isbn.lower():
                return book
        return None

    def exists(self, isbn):
        return self._find_by_id(isbn) != None

        


         

