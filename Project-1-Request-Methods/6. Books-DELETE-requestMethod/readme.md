## DELETE HTTP Method
* Delete the data
* PUT can have a body that has additional information like POST that GET requests do not have. For example we can pass the information to update the title/author/category of an existing book. 

    - eg: category from math to social
    > {"title": "Title Six", "author": "Author Two", "category": "social"}

* It will update the data to the body (of variable eg: BOOKS). So, we need to import `Body` funtionality from FastAPI