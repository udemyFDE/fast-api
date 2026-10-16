from fastapi import FastAPI, HTTPException

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")

async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")

async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

    # use this to explicitly return 404 if the parameters are not related to the function
    # raise HTTPException(
    #     status_code=404,
    #     detail=f"No book found with the title '{book_title}'"
    # )

# # Order of the functions matters
# @app.get("/books/mybook")
#
# async def read_all_books():
#     return {'book_title': 'My_favourite_Book'}

# # so, if anything is passed other than mybook after /books/<> it will call the dynamic param function
# # using the dynamic path parameters, the api can be consumed and be able to return the user what he types in
# @app.get("/books/{dynamic_param}")
#
# async def read_all_books(dynamic_param: str):   # str means dynamic_param must be a string
#     return {'dynamic_param': dynamic_param}


# # here /books/mybook is a static variable
# # the below app will not be called as the above function also has the same api with dynamic param
# # so, when we use /books/mybook then mybook will be treated as dynamic param
# # it will be processed by that function and will get the output as dynamic_param: mybook
# # to avoid this keep this function before the dynamic param function
# @app.get("/books/mybook")
#
# async def read_all_books():
#     return {'book_title': 'My_favourite_Book'}