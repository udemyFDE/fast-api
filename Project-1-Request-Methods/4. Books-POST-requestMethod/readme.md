## POST HTTP Method
* Create the data
* POST can have a body that has additional information that GET requests do not have. For example we can pass the information to add a new book.
> {"title": "Title Seven", "author": "Author Four", "category": "social"}
* It will create/add the data to the body (of variable eg: BOOKS). So, we need to import `Body` funtionality from FastAPI