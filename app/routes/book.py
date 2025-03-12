from uuid import uuid4
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from app.schemas import Book
import app.services.book as service

router = APIRouter(prefix="/books", tags=["Books"])

@router.get('/')
def get_all_books():
    books = service.get_all_books()
    return JSONResponse(
        content=[book.dict() for book in books],
        status_code=status.HTTP_200_OK,
    )

@router.get('/{book_id}')
def get_book(book_id: str):
    book = service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this ID",
        )
    return JSONResponse(book.dict())

@router.post('/')
def create_new_book(name: str, author: str, publisher: str):
    new_book_data = {
        "id": str(uuid4()),
        "name": name,
        "author": author,
        "publisher": publisher,
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid data for the book",
        )
    service.create_book(new_book)
    return JSONResponse(new_book.dict())

@router.put('/{book_id}')
def update_book(book_id: str, updated_data: dict):
    updated_book = service.update_book(book_id, updated_data)
    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this ID",
        )
    return JSONResponse(updated_book.dict())

@router.delete('/{book_id}')
def delete_book(book_id: str):
    deleted = service.delete_book(book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this ID",
        )
    return JSONResponse({"detail": "Book deleted successfully"})
