## Project - 2

* We still work with the API endpoints using below HTTP request methods used in [_project-1_](../Project-1-Request-Methods)
    - GET
    - POST
    - PUT
    - DELETE

* Also include:
    - Data validation
    - exception handling (partially used in [_project-1_](../Project-1-Request-Methods))
    - status codes (partially used in [_project-1_](../Project-1-Request-Methods))
    - swagger configuration
    - Python request objects.

* we're still going to be working with books. But these books are going to be real Python objects. To be able to do this, we need to create a new class called Book. In this new class that we call book is going to be the object of books that we're going to use throughout this project.


#### General Info

`Pydantic v1` vs `Pydantic v2`

* FastAPI is now compatible with both Pydantic v1 and Pydantic v2.

* Based on how new the version of FastAPI you are using, there could be small method name changes.

* The three biggest are:

    - `.dict()` function is now renamed to `.model_dump()`
    - `schema_extra` function within a Config class is now renamed to `json_schema_extra`
    - Optional variables need a `=None` example: `id: Optional[int] = None`