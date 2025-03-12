# FastAPI Library Management App

## Description
This is a simple FastAPI application for managing a library of books. Users can view the list of books, add new books, update existing ones, and delete books. Each book has a name, an ID, an author, and a publisher.

## Routes
- **GET /books**: Get the list of all books.
- **GET /books/{book_id}**: Get details of a specific book by ID.
- **POST /books**: Add a new book. Requires JSON payload with name, author, and publisher.
- **PUT /books/{book_id}**: Update details of a specific book by ID. Requires JSON payload with updated data.
- **DELETE /books/{book_id}**: Delete a book by ID.

## How to Run
1. Set up a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate `
   - On Windows: If the activation command doesn't work, you may need to change the execution policy to RemoteSigned using the following command:  `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
   - On macOS/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python main.py`

