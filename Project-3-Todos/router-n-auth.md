## Setting up authentication

* `main.py` the file to run our application, having everything included in it make it messy.

* We can use a different file for other APIs (eg: `auth.py` for authnetication API). But the problem with this is when the application from `main.py` is running we don't see/access the authentication API from `auth.py` which needs a separate port to run than our main.py file.

* To address this, we can use `Routers` &rarr; helps us organize the API endpoints into separate files instead of putting everything in main.py.

    - a way for us to be able to have a main file, the root of our application and then what sits on top of the main file are all these different routes which will lead to different fast API files, which will have their own APIs and API endpoints.
    
    - This allows to run our main.py and auth.py APIs on the same port, also allow our fast API application to really be able to be scalable and maintainable.

    - In the `PyCharm` &rarr; `right click` on the project-3 folder where we have the `main.py` file  &rarr; New &rarr; `Python Package` &rarr; name the package as `eg: routers` &rarr; under it create the files for authentication (eg: auth.py).

    - For scalable routers -- keep only router details in `main.py` while all the APIs sit inside the router files `todos.py` &rarr; `for application APIs` and `auth.py` &rarr; `for authentication APIs`. While using routers, `@app` will be replaced with `@router` for all API endpoints in the router file. And now the `main.py` file will have `eg: app = FastAPI()` while the router files will have `eg: router = APIRouter()`.

    >**Note:** After having all the content of main.py to router file and leaving the main.py file with only router reference, the imports in the router file need to be verified for appropriate directory structure. No issue if followed the structure as in this repo
