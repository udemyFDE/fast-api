### Basic SQL queries

* `Insert/Create/Add` data to a dabase table (todos --> example table name in the below queries)

```
INSERT INTO todos (title, description, priority, complete)

VALUES ('Go to store', 'To pickup eggs', 4, False);
```
> Here, we're not adding the Id because we want the DB to handle this and auto increment. For that we have set the primary key and index as True for Id in the model.py

> In databases; 0 = False, 1 = True --> these boolean values are for the complete column

* `Reading/Fetching` the data:

    - `SELECT` SQL queries
        - To get the data in a table
        ```
        SELECT * FROM todos;
        ```
        > (*) means all rows and columns

        - To get any one specific column
        ```
        SELECT title FROM todos;
        ```

        - To get more than one column
        ```
        SELECT title, description FROM todos;
        ```
        ```
        SELECT title, description, priority FROM todos;
        ```
    
    - `WHERE` SQL queries
        - To get the data in a table using a filter
        ```
        SELECT * FROM todos WHERE pririty=5;
        ```
        > This will give all the records (rows) that matches the priority with all columns

        ```
        SELECT * FROM todos WHERE title='Go to store';
        ```
        >  This will give all the records (rows) that matches the title with all columns.

        ```
        SELECT * FROM todos WHERE id=2;
        ```
    
* `Updating` the records/data in the database
    - `UPDATE` SQL queries
    ```
    UPDATE todos SET complete=True WHERE id=5;
    ```
    > Update all rows and columns to now have complete = True where id=5. Most practical and best way to update a record is to always locate the record by the primary key because the primary key is going to be unique. 
    
    - However, it is possible to push an update when not talking about the ID.
    ```
    UPDATE todos SET complete=True WHERE title='Learn something new';
    ```
    > The issue with this approach is that there could be more than one record that can has the same title and will update all the records with the matching title which means the title is not unique. So if we want to use this approach, always remember that we know the title is not a unique name. Therefore, we could be changing multiple records to true.


* `Deleting` the records/data in the database
    - `DELETE` SQL queries
    - Again, the best way of deleting a single record is by the primary key, which in this case is the ID.
    ```
    DELETE FROM todos WHERE id=5;
    ```
    > after the statement gets executed, the record with the ID of five is completely deleted.

    >If you do not want to completely remove it, a user has a history of deleted records. The application will create a table that holds, quote unquote deleted records. This way, things are not permanently erased, but just removed from the table of the mean application and move to another table where the table still exists.

    - And as always, we do not have to delete based on ID or a primary key, even though it is significantly more safe.
    ```
    DELETE FROM todos WHERE complete=0;
    ```
    >This will delete all rows and columns, where complete is equal to zero. So if we do not change any of our complete areas to true, we would essentially erase and delete our entire database. This is the risk in using the delete functionality when not using it by a primary key to delete a specific record.

* Above are the most popular commands when dealing with CRUD operations in case you want to manipulate the data yourself `manual`.

* `SQLAlchemy` handles a lot of these commands on the application side, so we don't have to worry about running the commands ourselves to manipulate the data.