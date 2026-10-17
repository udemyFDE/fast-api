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

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# Pydantic Model for data validation
class BookRequest(BaseModel):
    # id: Optional[int] = None  # instead of having just None, can add description with default = None
    id: Optional[int] = Field(description="Id is not required on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, lt=6)

    # Instead of just having the data types as example values
    # this will populate the meaningful statements
    # As Id is automated and not defined here, it will also be not visible in the example value in swagger UI
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Title of new book",
                "author": "Author name of new book",
                "description": "Description of new book with max characters as 100",
                "rating": 4
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1)
]

@app.get("/books")

async def read_all_books():
    return BOOKS


# POST using Pydantic model as the input for validating the request to add the book
# due to BookRequest (pydantic model class) we see the schema that needs to be passed
@app.post("/create_book")

async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


