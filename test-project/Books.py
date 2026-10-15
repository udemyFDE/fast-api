from fastapi import FastAPI

app = FastAPI()
# this allows uvicorn to identify that we are creating a new app of FastAPI
# and is importing all of the resources we got using import on top

# for fast API to acknowledge that this is an API endpoint.
# How can we now call this using our appropriate API verbs?
# so we create a decorative

@app.get("/test-books")

# this is the function
async def testbooks_api():
    return {"message": "Hello World..!"}
# even if `async' which stands for asynchronous and is optional for FastAPI