## Alembic Data Migration

![alt text](./images/what-is-alembic.png)

> We have seen in earlier section SQL Alchemy already created our tables for our application because there was no data for that specific table. But Alembic will allow us to be able to add a column to our database table within our application without having to delete our table or anything like that to allow SQL alchemy to work.

![alt text](./images/how-does-alembic-work-1.png)

* So as of now, we already have some data within our database. Let's take a look at our current users table. For this example, we take our users table which has an ID, username, email, first_name, last_name, hashed passwords, role, is_active. Now we want to add a new column on our data that already exists. Let's say adding a phone number, so in our users table, instead of having to delete the data, we are just going to add a new column of phone number.

![alt text](./images/how-does-alembic-work-2.png)

## Using Alembic

* Install Alembic into our project.
```
pip install alembic
```

![alt text](./images/how-does-alembic-work-3.png)

![alt text](./images/how-does-alembic-work-4.png)

![alt text](./images/alembic-ini.png)

![alt text](./images/alembic-directory.png)