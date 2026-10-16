from fastapi import FastAPI

app = FastAPI()
# this allows uvicorn to identify that we are creating a new app of FastAPI
# and is importing all of the resources we got using import on top


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


# for fast API to acknowledge that this is an API endpoint.
# How can we now call this using our appropriate API verbs?
# so we create a decorative

@app.get("/books")

# this is the function
async def read_all_books():
    return BOOKS
# even if `async' which stands for asynchronous and is optional for FastAPI