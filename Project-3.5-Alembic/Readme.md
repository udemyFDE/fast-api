## Alembic Data Migration

* [_What is Alembic_](#what-is-alembic)
* [_How to use Alembic_](#using-alembic)
* [_Setting up Alembic_](#setting-up-alembic)
* [_Alembic Revision_](#alembic-revision)
    - [_alembic upgrade_](#alembic-upgrade)
    - [_alembic downgrade_](#alembic-downgrade)

### What is Alembic?

![alt text](./images/what-is-alembic.png)

* We have seen in earlier section SQL Alchemy created tables (data, .db file) for our application when there was no data (table) already exist. 

* To change/update the table we need to delete the .db file and need to run the app again after updating/adding the columns in models.py. 

* If we update/add the column in models.py and run the application without deleting the existing .db file already created with earlier columns, we see the internal server error as the exsiting .db file will not have the updated columns. 

* But Alembic will allow us to be able to add a column to our database table within our application without having to delete our table or anything like that to allow SQL alchemy to work.

![alt text](./images/how-does-alembic-work-1.png)

* So as of now, we already have some data (table) within our database. Let's take a look at our current users table. For this example, we take our users table which has an ID, username, email, first_name, last_name, hashed passwords, role, is_active. Now we want to add a new column on our data that already exists. Let's say adding a phone number, in our users table, instead of having to delete the data, we are just going to add a new column of phone number.

![alt text](./images/how-does-alembic-work-2.png)

### Using Alembic

![alt text](./images/how-does-alembic-work-3.png)

> revision # --> here # stand for Id (revsion Id)

![alt text](./images/how-does-alembic-work-4.png)

![alt text](./images/alembic-ini.png)

![alt text](./images/alembic-directory.png)


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


### Alembic Revision

![alt text](./images/alembic-revision.png)

#### Alembic Upgrade

![alt text](./images/alembic-upgrade-1.png)

> None --> to expect a response of nothing (no response from the function).

> user --> table name; phone_number --> coloumn to add with nullable set to True becuase immediatlely there's not going to be any data or the users already in the table have no phone numbers entered.

> sa --> SQLAlchemy

![alt text](./images/alembic-upgrade-2.png)


#### Alembic Downgrade

![alt text](./images/alembic-downgrade-1.png)

![alt text](./images/alembic-downgrade-2.png)

> -1 --> to revert to last migration