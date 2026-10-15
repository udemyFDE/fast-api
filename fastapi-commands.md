## Commands to run the application or api

* Open PyCharm and open the directory where the virtual environment is created and activated. Suppose the working directory is `D:\temp\fastapi` and the virtual environment `fastapivenv` is created under it then `D:\temp\fastapi` should be opened from PyCharm.

* Open the terminal in PyCharm and ensure the virtual environment is activated. 

* Run the below command (the .py extension is not required). `app` is the decorative used to call the endpoint

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

* As we used `--reload` in the command, when we update anything in the file and save, it automatically restart the application (provided if the changes are made when the application is running )

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
- the `fastapi` command also run the `uvicorn` command in the backend.

* To stop the application hit `Ctrl+C`

* The url can be accessed when the app is running.

* FastAPI also has `swagger UI` which is automatically implented with it. Swagger will allow us to see all of our api enpoints. We'll be able to call our api endpoints and see the response of each api endpoint. For that we need to replace the api endpoint with `docs`. For example: if the api endpoint is `/books` after `http://127.0.0.1/books` then to access using swagger use `http://127.0.0.1/docs`. In the swagger UI, you will see the api endpoint --> try out --> execute. We can see the request url, response code, response body,response header.... under the responses