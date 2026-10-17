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
# Need to import BaseModel, not accept the values of different data type than defined
# import Field, to add validation of values. Can be seen in schema under the respective Method in Swagger UI
# if the values are passed than what is accepted, error -- unprocessable entity
class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, lt=6)


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
    # print(type(book_request)) # it will give as BookRequest (pydantic model), eg: <class 'Books.BookRequest'>
    # new_book = Book(**book_request.dict()) # dict() is deprecated, not work on new versions
    # .dict() or -model_dum() - return all the variables in dictionary format
    # ** convert the request to Book object by expanding the dictionary keys and values into the arguments required for the constructor
    new_book = Book(**book_request.model_dump())
    # print(type(new_book))   # now we get type as Book instead of BookRequest <class 'Books.Book'>
    # BOOKS.append(new_book)
    BOOKS.append(find_book_id(new_book))    # the book Id is passed from find_book_id function below

# We're accepting a request of BookRequest from pedantic, so our body must match this BookRequest object.
# We are transforming this BookRequest into a book object that we're using as our source of truth.
# And then we're adding it to our list of books.
# we can add even more data validation for each field
# So our ID or title author description and rating saying that a rating can't be over 100 or IDs can't
# be -50.


# Book is the class object defined above which give the properties to be initialized
def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book



# # using Body() do not add any validation to the application
# # It will create the object with whatever values are supplied
# # for example, Books should have the Id incremented value and not like (-09 / -99..)
# # Also, the rating should be from 1 to 5/10 but not a negative value
#
# @app.post("/create_book")
#
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)

