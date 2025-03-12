from app.schemas import Book
from app.database import database


def get_all_books() -> list[Book]:
    books_data = database["books"]
    books = [Book.model_validate(data) for data in books_data]
    return books


def get_book_by_id(book_id: str) -> Book | None:
    selected_book = [
        book for book in database["books"]
        if book["id"] == book_id
    ]
    if len(selected_book) < 1:
        return None
    selected_book = Book.model_validate(selected_book[0])
    return selected_book


def create_book(new_book: Book) -> Book:

    if not new_book.name.strip() or not new_book.author.strip() or not new_book.publisher.strip():
        raise ValueError("Name, author, and publisher must not be empty or contain only spaces")
    database["books"].append(new_book.dict())
    return new_book


def update_book(book_id: str, updated_data: dict) -> Book | None:
    for i, book in enumerate(database["books"]):
        if book["id"] == book_id:
            database["books"][i].update(updated_data)
            updated_book = Book.model_validate(database["books"][i])
            return updated_book
    return None



def delete_book(book_id: str) -> bool:
    initial_length = len(database["books"])
    database["books"] = [book for book in database["books"] if book["id"] != book_id]
    final_length = len(database["books"])
    return final_length < initial_length
