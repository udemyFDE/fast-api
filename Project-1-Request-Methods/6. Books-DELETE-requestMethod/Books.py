from fastapi import FastAPI, HTTPException, Body
from pygments.lexer import default

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# GET Method
@app.get("/books")

async def read_all_books():
    return BOOKS


# GET Method with path parameter
@app.get("/books/{book_title}")

async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


# GET Method with query parameter
@app.get("/books/")

async def read_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    if len(books_to_return) > 0:
        return books_to_return
    else:
        return books_to_return

# GET Method with path and query parameters
@app.get("/books/{book_author}/")

async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    final_books = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)

    if len(books_to_return) > 0:
            for item in books_to_return:
                if item.get('category').casefold() == category.casefold():
                    final_books.append(item)

            if len(final_books) > 0:
                return final_books
            else:
                return final_books

    else:
        return books_to_return


# POST method

@app.post("/books/create_book")

# async def create_book(new_book=Body()):
#     BOOKS.append(new_book)

# OR

async def create_book(new_book=Body()):
    for book in BOOKS:
        if book["title"].casefold() == new_book["title"].casefold():
            raise HTTPException(
                status_code=409,
                detail=f"Book already exists with title: '{book.get('title')}', author: '{book.get('author')}', "
                       f"category: '{book.get('category')}'"
            )

    BOOKS.append(new_book)
    return {
        "message": "Book created successfully",
        "book": new_book
    }


# PUT Method

@app.put("/books/update_book")

# taking the title as reference, update author and/or category
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            return {
                "message": "Book updated successfully",
                "book": updated_book
            }

    raise HTTPException(
        status_code=404,
        detail=f"Book title '{updated_book.get('title')}' not found"
    )

# DELETE Method

@app.delete("/books/delete_book/{book_title}")

async def delete_book()