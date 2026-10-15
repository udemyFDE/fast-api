## Commands to run the application or api

* Open the terminal in PyCharm and ensure the virtual environment is activated

* Run the below command (the .py extension is not required). `app` is the decorative that we used

```
uvicorn <name of the .py file>:app --reload
```

eg:
>uvicorn Books:app --reload


> OR

```
uvicorn <name of the .py file>:app --reload --app-dir <path of the directory where the file exist file>
```

> uvicorn test-project/Books:app --reload

* The above command will run the application and give the url. Open it in the browser and if required, append `/<api endpoint>` if any added for the app.

eg: `http://127.0.0.1:8000` OR `http://127.0.0.1:8000/test-books`

* If using the new versions of FastAPI, we can run the app using the below command in `production mode`. To run in `development mode` replace `run` with `dev`

```
fastapi run <file.py>
```
```
fastapi dev <file.py>
```
eg:
> fastapi run Books.py

Or

```
fastapi run <directorypath/file.py>
```
```
fastapi ev <directorypath/file.py>
```
eg:
> fastapi run test-project/Books.py

- The URLs for each mode will be 
    - `production mode` -- `http://0.0.0.0:8000`
    - `development mode` -- `http://127.0.0.1:8000`