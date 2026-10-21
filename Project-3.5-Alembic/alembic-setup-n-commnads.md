### Setting up Alembic


* Install Alembic into our project.
```
pip install alembic
```
* In the project folder, run 
```
alembic init <environment name>
```

environment name --> similar to a virtual enviornment we created for FastAPI
> alembic init alembic

* In `alembic.ini` we need to update the `sqlalchemy.url` to point to our database that we try to add the configuration and migrations for.

> defaut --> sqlalchemy.url = driver://user:pass@localhost/dbname

> update to use our .db file --> sqlalchemy.url = sqlite:///./database/todosapp.db

> **Note:** the value has no qoutes unlike in the database.py

* In `alembic/env.py`, we need
    - import models.py
    - comment the below lines, we don't need the condition. So just keep the `fileConfig(config.config_file_name)` and remove the space before it.
    ```
    if config.config_file_name is not None:
        fileConfig(config.config_file_name)
    ```
    - Change `target_metadata = None` to `target_metadata = models.Base.metadat`


### Alembic Revision -- upgrade/downgrade

* Now, run the below command to create a revision.

```
alembic revision -m "message"
```
> This will create .py file inside the /alembic/versions/ which has the message as file name and a unique revision Id. Thi file also has default functions for upgrade and downgrade with just `pass`

* We need to write our code/logic for our revisions in this file

* In the `upgrade` function within the auto created file in /alembic/versions/, comment/remove the default value `pass` and add the below.

eg: to add phone_number column
```
op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
```

* Now, run the below command to upgrade the table using the revision Id of the file in /alembic/versions/

```
alembic upgrade <revision id>
```
eg: 
>alembic upgrade e0d0df7075d0

* Once the upgrade is done, can verify it in the database table. But it will not be visible in the swagger unless the same column is added to `models.py`. Adding in models.py without upgrade will throw the error.