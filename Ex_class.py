class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book.display_info()
        return "Book not found"

    def borrow_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                return self.books.pop(i).display_info()
        return "Book not found"

# 도서 생성
book1 = Book("1984", "George Orwell", "978-0451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789")

# 도서관 생성 및 도서 추가
my_library = Library()
my_library.add_book(book1)          # book1 인스턴스의 참조가 my_library 인스턴스 리스트 안에 저장됨. 중요한 것은 실제 값이 아니라 참조(주소)가 저장되었다는 것
my_library.add_book(book2)

# 도서 정보 출력
print(my_library.find_book_by_title("1984"))

# 도서 대출
print(my_library.borrow_book("1984"))
print(my_library.find_book_by_title("1984"))  # 대출 후 다시 검색