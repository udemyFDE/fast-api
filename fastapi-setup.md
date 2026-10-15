## FastAPI and Virtual environment setup/installation (Windows)

* Prerequisites
    - Python

    open command prompt - validate if python is installed
    ```
    python --version
    ```
    - pip -- package manager for pytnon (come with python installation)

    ```
    python -m pip --version
    ```

* Pip List willshow us everything that we have downloaded on our machine without using a virtual environment.
```
pip list
```

* Go to the target working directory `cd <path>`. create a new directory `mkdir <name>` and `cd` to it and run the belwo command to create a virtual environment.

eg: 
>c:\Users\test\fastapi

```
python -m venv <name>
```
eg:
>python -m venv fastapivenv

* Activate the virtual environment so that we can install FastAPI

```
<name>\Scripts\activate.bat
```
eg:
>fastapivenv\Scripts\activate.bat

- this will activate the environment can see in the terminal

```
<name> <working directory>
```
eg:
>(fastapivenv) c:\Users\test\fastapi

* Insatll FastAPI
```
pip install fastapi
```

* Install uvicorn (web server for FastAPI)
```
pip install "uvicorn[standard]"
```

* can validate using `pip list` command

* To deactivate the environment
```
deactivate
```

    - now we'll see only the working directory

    eg:
    c:\Users\test\fastapi

    - and not this

    eg:
    (fastapivenv) c:\Users\test\fastapi

* To delete the virtual environment, ensure the working directory is pointing to the parent directory (eg: c:\Users\test\fastapi) of virtual environment forder name and run the below command

```
rmdir /s /q <name>
```
- /s — deletes the folder and all its contents.

- /q — deletes without asking for confirmation.

eg:
> rmdir /s /q fastapivenv