'''

Add a new field to Book and BookRequest called published_date:
int (for example, published_date: int = 2012).
So, this book as published on the year of 2012.
Enhance each Book to now have a published_date
Then create a new GET Request method to filter by published_date

'''


from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional


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
    # id: Optional[int] = None  # instead of having just None, can add description with default = None
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

    # Instead of just having the data types as example values
    # this will populate the meaningful statements
    # As Id is automated and not defined here, it will also be not visible in the example value in swagger UI
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

@app.get("/books")

async def read_all_books():
    return BOOKS

# Get by published year

# @app.get("/books/{published_year}")

@app.get("/books/published_year/")
async def read_book_year(published_year: int):
    books_to_return = []
    # for i in range(len(BOOKS)):
    #     if BOOKS[i].published_date == published_year:
    #         books_to_return.append(BOOKS[i])
    for book in BOOKS:
        if book.published_date == published_year:
            books_to_return.append(book)
    return books_to_return



# Fetch book by Id using path parameter
@app.get("/books/{book_id}")

async def read_book(book_id: int):
    for book in BOOKS:
        if book_id == book.id:
            return book


# Fetch books by rating

# path parameter -- Order matters
# to use it keep this function before the Id function above or comment it
# @app.get("/books/{rating}")
# async def read_books_by_rating(rating: int):
#     return [book for book in BOOKS if book.rating >= rating]

# query parameter
@app.get("/books/")
async def read_books_by_rating(rating: int):
    return [book for book in BOOKS if book.rating >= rating]


# POST using Pydantic model as the input for validating the request to add the book
# due to BookRequest (pydantic model class) we see the schema that needs to be passed
@app.post("/create_book")

async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


# PUT method to update the BOOKS using Id
@app.put("/books/update_book")

async def update_book(book: BookRequest):   # BookRequest is a pydantic object
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


# DELETE method to delete the book using Id
@app.delete("/books/{book_id}")

async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break