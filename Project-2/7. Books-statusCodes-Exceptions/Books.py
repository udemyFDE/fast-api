'''

In this, we learn about the Status codes and HTTP exceptions
Need to import HTTPException from FastAPI
For explicit Status code responses -- require Status to be imported from Starlette
Starlette will be installed when we install FastAPI

'''


from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status


app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# Pydantic Model for data validation
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not required on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, lt=6)
    published_date: int = Field(
        ge=1800,
        le=2299,
        description="The year the book was published"
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Title of new book",
                "author": "Author name of new book",
                "description": "Description of new book with max characters as 100",
                "rating": 4,
                "published_date": 2015
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2010),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2001),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 1856),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 1924),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2010),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2019)
]

# for GET methods status_code=status.HTTP_200_OK, return data
# for POST methods status_code=status.HTTP_201_CREATED, create
# for PUT and DELETE methods status_code=status.HTTP_204_NO_CONTENT
# for PUT and DELETE, we'll not create or return but only enhance or change

@app.get("/books", status_code=status.HTTP_200_OK)

async def read_all_books():
    return BOOKS


@app.get("/books/published_year/", status_code=status.HTTP_200_OK)
async def read_book_year(published_year: int = Query(ge=1800, le=2299)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_year:
            books_to_return.append(book)

    if len(books_to_return) > 0:
        return books_to_return
    else:
        raise HTTPException(
            status_code=404,
            detail=f"No Book found with published year: {published_year}"
        )



@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)

async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book_id == book.id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Item Not Found"
        # detail = f"Book with Id: {book_id} not Found"
    )


# Fetch books by rating

# path parameter -- Order matters
# to use it keep this function before the Id function above or comment it
# @app.get("/books/{rating}", status_code=status.HTTP_200_OK)
# async def read_books_by_rating(rating: int = Path(gt=0, le=5)):
#     return [book for book in BOOKS if book.rating >= rating]

# query parameter
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(rating: int = Query(ge=1, le=5)):
    return [book for book in BOOKS if book.rating >= rating]

    raise HTTPException(
        status_code=404,
        detail=f"No Book found with the rating {rating} or above"
    )


# POST using Pydantic model as the input for validating the request to add the book
# due to BookRequest (pydantic model class) we see the schema that needs to be passed
@app.post("/create_book", status_code=status.HTTP_201_CREATED)

async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


# PUT method to update the BOOKS using Id
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)

async def update_book(book: BookRequest):  # BookRequest is a pydantic object
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
            return {
                "Message": f"Book with Id: {book.id} updated successfully",
                "Updated Book": book.model_dump()
            }

    if not book_changed:
        raise HTTPException(
            status_code=404,
            # detail="Item Not Found"
            detail=f"Book with Id: '{book.id}' not Found"
                   # f"{book.model_dump()}"
        )
# OR

# async def update_book(book: BookRequest):   # BookRequest is a pydantic object
#     for i in range(len(BOOKS)):
#         if BOOKS[i].id == book.id:
#             BOOKS[i] = book
#
#     raise HTTPException(
#         status_code=404,
#         # detail="Item Not Found"
#         detail = f"Book not Found"
#                  f"{Book}"
#     )

# DELETE method to delete the book using Id
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_book(book_id: int = Path(gt=0, lt=len(BOOKS))):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            deleted_book = BOOKS[i]
            BOOKS.pop(i)
            book_changed = True
            return {
                "Message": f"Book with given Id: {book_id} deleted successfully",
                "Deleted Book": deleted_book
            }
            break
    if not book_changed:
        raise HTTPException(
            status_code=404,
            # detail="Item Not Found"
            detail=f"Book with Id: '{book_id}' not Found"
        )