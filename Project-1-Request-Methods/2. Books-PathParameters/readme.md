## Path Parameters
* Path parameters are request parameters that have been attached to the URL. They are usually defined as a way to find information based on location.

* So let's think of a computer file system.You can identify the specific resource based on the file in the path you are in.

* In Books.py example we have the list of Books and an api enpoint as `/books` which is and matches the request url `http://127.0.0.1/books`. This will give us all the books and it is the static path and cannot be changed.

* We can also make use of dynamic path parameters. Let's say we have a request `http://127.0.0.1/books/book_one`. Here the `book_one` is what the user types in (can be book_two and so on). So, we can't have an api endpoint for each request. By using a dynamic parameter in the application function, whatever is passed for dynamic parameter nad if it matches the url will return that specifc value from books.

```
@app.get("/books/{dynamic_param}")

async def read_all_books(dynamic_param):
    return {'dynamic_param': dynamic_param}
```

**Order matters with the path parameters** 
* Let's say we have the request `http://127.0.0.1/books/my_book` and if we have a specific function for it (below example). Then my_book in the request will be transformed into the dynamic_param of 1st funtion and the 2nd function will not be called because the 1st one is accepting the same parameter list.

```
@app.get("/books/{dynamic_param}")

async def read_all_books(dynamic_param):
    return {'dynamic_param': dynamic_param}

@app.get("/books/my_book")

async def read_all_books():
    return {'Book_title': 'My_favourite_book'}

```
* So, always have the static / smaller APIs in front/at the top.

```
@app.get("/books/my_book")

async def read_all_books():
    return {'Book_title': 'My_favourite_book'}

@app.get("/books/{dynamic_param}")

async def read_all_books(dynamic_param):
    return {'dynamic_param': dynamic_param}

```

* If the request is to call by a specific name/title/otherinfo that can have a space then use `%20` (encodes the space) to fill the space. for example, if the request is `http://127.0.0.1/books/title one` then it will fail, need to be `http://127.0.0.1/books/title%20one`
