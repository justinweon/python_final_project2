from book import Book
from library import Library
import specialized_books
import traceback

def main():
    lib = Library()
    while True:
        try: 

            print()
            print("🏛️=== Book library menu===🏛️")
            print()
            print("🔍 도서 검색")
            print("➕ 도서 등록")
            print("📤 도서 대여")
            print("📥 도서 반납")
            print("📚 모든 도서 보기")
            print("❌ 나가기")
            print()
            print("+ ".center(20, "-"))

            choice = input("원하는 기능의 번호를 선택하세요👉").strip()
            print()

            if choice == "1":
                print("도서 검색")
                term = input("검색어를 입력하세요:").strip()
                matches = lib.search_books(term)
                if matches:
                    title = [book.get_title() for book in matches]
                    print(f">>{', '.join(title)} 🔍검색되었습니다.")

                else:
                    print("검색결과가 없습니다.")

            elif choice == "2":
                print("2. 도서 등록")
                isbn = input("도서번호:").strip()
                title = input("도서 제목:").strip()
                author = input("저자:").strip()

                if lib.exists(isbn):
                    print("이미 등록된 도서입니다")
                    continue

                book_type = input("도서종류를 선택하세요 (1: 단행본  | 2: 전자도서)").strip()

                if book_type == "1":
                    pages = input("페이지 수:").strip()
                    new_book = specialized_books.Paperbook(title, author,isbn,pages)
                    lib.add_book(new_book)

                elif book_type =="2":
                    file_size = input("파일크기(MB):", "파일 크기는 숫자로 입력하세요").strip()
                    new_book = specialized_books.Ebook(title,author,file_size)
                    lib.add_book(new_book)
                    
                else:
                    print("올바른 도서종류 (1 또는 2)를 선택해주세요")


            elif choice == "3":
                print("도서 대여")
                isbn = input("대여하실 도서의 도서번호를 입력하세요.").strip()
                lib.borrow_books(isbn)

            elif choice == "4":
                b_id = input ("반납하실 도서의 도서번호를 입력하세요.").strip()
                lib.return_books(b_id)

            elif choice == "5":
                print("전체 도서 보기")
                lib.display_info()


            elif choice == "6":
                print("서비스를 종료합니다.")
                break

            else:
                print("1~6 사이의 번호를 선택해주세요.")

        except Exception as e:
            traceback.print_exc()
            print("에러:", e)
            print("메인 메뉴로 이동합니다.")

if __name__ =="__main__":
    main()
            

