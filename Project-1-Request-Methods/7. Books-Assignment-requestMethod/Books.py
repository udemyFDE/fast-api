'''
Create a new API Endpoint that can fetch all books from a specific author
using either Path Parameters or Query Parameters.
'''

from fastapi import FastAPI, HTTPException, Body

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
@app.get("/books/by_author/{author}")

async def read_book(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    if len(books_to_return) > 0:
        return {
            "message": f"Found the below books for author '{author}'",
            "books": books_to_return
        }
    else:
        return {"message": f"No book found for author '{author}'"}

# OR

# # GET Method with query parameter
# @app.get("/books/by_author/")
#
# async def read_author(author: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == author.casefold():
#             books_to_return.append(book)
#
#     if len(books_to_return) > 0:
#         return {
#             "message": f"Found the below books for author '{author}'",
#             "books": books_to_return
#         }
#     else:
#         return {"message": f"No book found for author '{author}'"}
