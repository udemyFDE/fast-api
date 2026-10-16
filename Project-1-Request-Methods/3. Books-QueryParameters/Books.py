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


# In the path parameter, we are passing in something in the URL that we're converting
# to our parameter in our function
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

# Query parameter
# If anything that is passed in after books, that is not a dynamic path parameter.
# Fast API automatically converts into whatever parameters we have here within our function.
# here the api endpoint is ending with '/' slash unlike the above functions where the endpoint is like /books
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
        # use this to explicitly return 404 if the parameters are not related to the function
        # raise HTTPException(
        #     status_code=404,
        #     detail=f"No book found with the category '{category}'"
        # )


# using path and query parameters in same function
# here the api endpoint is ending with '/' slash so that it accept both path (dynamic) and query parameters
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
                # use this to explicitly return 404 if the parameters are not related to the function
                raise HTTPException(
                    status_code=404,
                    detail=f"No book found with author '{book_author}' and the category '{category}'"
                )
    else:
        return books_to_return
        # use this to explicitly return 404 if the parameters are not related to the function
        # raise HTTPException(
        #     status_code=404,
        #     detail=f"No book found with the author '{book_author}'"
        # )
