### Install SQLite3 on Windows

* Install SQLite on a Windows operating system so we can manipulate the data of a database, be able to select all from a database and be able to just completely be able to use a SQLite database from the terminal.
* link &rarr; https://www.sqlite.org/ &rarr; click on `Download` &rarr; select the last one `sqlite-tools-win-x64-xxx.zip` under `Precompiled Binaries for Windows`
* Once downloaded, `extract` and `copy` the folder to C:\ drive and rename to `sqlite3`
* Add the it the `PATH` in system environment variables.
* Open `comman prompt` and run `sqlite3`, this should connect to the `transient in-memory database`
* To exit runt `.exit` or `.quit`

* To connect with the db created (todos.db file) from the terminal, from the project folder `D:\udemy\FDE\FAST-API`

```
sqlite3 .\database\todos.db
```
> OR, if the working directory is set to the databse folder `D:\udemy\FDE\FAST-API\database`

```
sqlite3 todos.db
```

* Check schema
```
.schema
```
> This will show the info about the tables that we have in the database.

* Add records
    ```
    insert into todos (title, description, priority, complete) values ('Go to the store', 'pickup eggs', 5, False);
    ```
- Adding multiple values
    ```
    insert into todos (title, description, priority, complete) 
    values ('Cut the lawn', 'grass is getting long', 3, False),
           ('Feed the dog', 'he is getting hungry', 5, False);
    ```

* Read the data
    ```
    select * from todos;
    ```
