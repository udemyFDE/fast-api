## Alembic Data Migration

![alt text](./images/what-is-alembic.png)

* We have seen in earlier section SQL Alchemy created tables (data, .db file) for our application when there was no data (table) already exist. 

* To change/update the table we need to delete the .db file and need to run the app again after updating/adding the columns in models.py. 

* If we update/add the column in models.py and run the application without deleting the existing .db file already created with earlier columns, we see the internal server error as the exsiting .db file will not have the updated columns. 

* But Alembic will allow us to be able to add a column to our database table within our application without having to delete our table or anything like that to allow SQL alchemy to work.

![alt text](./images/how-does-alembic-work-1.png)

* So as of now, we already have some data (table) within our database. Let's take a look at our current users table. For this example, we take our users table which has an ID, username, email, first_name, last_name, hashed passwords, role, is_active. Now we want to add a new column on our data that already exists. Let's say adding a phone number, in our users table, instead of having to delete the data, we are just going to add a new column of phone number.

![alt text](./images/how-does-alembic-work-2.png)

## Using Alembic

![alt text](./images/how-does-alembic-work-3.png)

![alt text](./images/how-does-alembic-work-4.png)

![alt text](./images/alembic-ini.png)

![alt text](./images/alembic-directory.png)


## Setting up Alembic


* Install Alembic into our project.
```
pip install alembic
```
* In the project folder, run 
```
alembic init <environment name>
```

environment name --> similar to a virtual enviornment we created for FastAPI
>alembic init alembic