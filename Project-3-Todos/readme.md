## Project three

* we will be switching our focus to doing `TODOS` instead of using `BOOKS` as our primary object.
* To create this project, in the `PyCharm` &rarr; `right click` on the parent folder where we have the virtual environment &rarr; New &rarr; `Python Package` &rarr; Name the project (eg: project-3-Todos)

* New information will include:
    - `Database`
        - Full `SQL database`. This database is going to have all of the records and tables that we need for a full fledged database.
        - We'll start this project with using `SQLite`, which is an easy embedded database and our application.
        - We then see step by step on how to use two extremely popular and production databases, `PostgreSQL` and `MySQL`.
    - `Authentication`
        - how we can get authentication with JWT and our application.
        - And that ultimately means being able to create users that have a username and password.
    - `Authorization`
        - roles and responsibilities where a user can be an admin and they get certain API endpoints available that other users do not get.
    - `Hashing Passwords`
        - As we deal with user authentication and authorization, we need to hash the password before we save them into the database.
        - step by step on how to create a hashing algorithm for our application to be able to hash all of the passwords that we save as records.


**Creating a Todo Table**
- we will create a new `Todo` table model for our application.
- We will be using these Todos to save records throughout this project.
- Once we have the required `database.py` and `models.py` files created in database folder, create a `main.py` in project folder and run the below commands.

```
cd <project folder>
```
eg:
> cd ./project-3-Todos

```
uvicorn main:app --reload
```
> This will create a .db file in the location (SQLALCHEMY_DATABASE_URL) specified in database.py file

- Once the db file is created, install `SQLite` to connect and manage the data.

**General Info**

`Pydantic v1` vs `Pydantic v2`

* FastAPI is now compatible with both Pydantic v1 and Pydantic v2.

* Based on how new the version of FastAPI you are using, there could be small method name changes.

* The three biggest are:

    - `.dict()` function is now renamed to `.model_dump()`
    - `schema_extra` function within a Config class is now renamed to `json_schema_extra`
    - Optional variables need a `=None` example: `id: Optional[int] = None`