## Introduction

![alt text](./productoin-DBMS-images/postgresql-intro.png)

* [_setup PostgreSQL on windows_](#setup-and-installation)
* [_setup SQL tables_](#create-a-database-tables)
* [_connect to FastAPI application_](#connect-to-fastapi-application)


### Setup and Installation

* Go to &rarr; https://www.postgresql.org/ &rarr; click on `Download` &rarr; select `windows` &rarr; click on `Download the installer` &rarr; select the version (latest) for `Windows x86-64`

* Once downloaded, open it to install and click on `Next` for all. Ensure all are selected in `select components` and enter a `supr user passwrod`. This will take a while to complete.

>**_Note_:** Just for information, after installation, it will ask for launching `stack builder` &rarr; `tick the box` and click on `finish` &rarr; In the stack builder, select the `PostgreSQL {version}(x64) on port 5432` from dropdown and click `next` &rarr; on the select applications tab, leave the default (not required for this excercise) and click `cancel` as clicking `next` requires to select at least one application.

* Open `pgAdmin` app, GUI for PostgreSQL, that is installed part of postgreSQL installation.

* Expand `servers` a default server group and click on the default server `PostgreSQL {version}`,created as part of the installation, to connect to the server and enter the password used during the installatoin.

### Create database tables
* Open `pgAdmin` app, we can create a new server group, but for this excersice we use the default server group `servers`.
* `Right click` on servers &rarr; Register &rarr; server.

![alt text](./productoin-DBMS-images/postgresql-1.png)

* provide the password (same one used for installing, as we are registering under the default server group)

![alt text](./productoin-DBMS-images/postgresql-2.png)

* Once done, expand the new server and `Login/Group Roles` and check the super user `postgres`. right click on super user and check all privileges are enabled.
![alt text](./productoin-DBMS-images/postgresql-3.png)

* If no super user exist, then we can create a new role by right clcking on `Login/Group Roles` &rarr; create &rarr; give a name and enable all privileges.

* Right click on `databases` &rarr; create database &rarr; give a name as `TodoApplicationDatabase` ans ensure the super user (default `postgres` or any custom role created) is selected as owner of the database.

* Once the DB is created, it will be connected automatically, if not we can right click and hit connect.

* Under the database &rarr; `Schemas` &rarr; `public` &rarr; `Tables` (can create the tables manually or using the query tool by right clicking it).

* In the `Query tool`, run the SQL code from the file [_PostgreSQL-script_](./Database%20Scripts/PostgreSQLScript.sql) which will create 2 tables `users` and `todos`.

### Connect to FastAPI application

* Install the below python library `psycopg2-binary`

```
pip install psycopg2-binary
```
>OR

```
pip install "psycopg[binary]"
```
> We may face an error when we run the application when SQLAlchemy tries to use psycopg (Psycopg 3), but if we installed psycopg2-binary (Psycopg 2). These are different PostgreSQL drivers.

* Now update the database URL `SQLALCHEMY_DATABASE_URL` that was used for SQLite DB for earlier exercise in `database.py`. Can comment it and add another one for `PostgreSQL`

if no error using `psycopg2-binary`
> 'postgresql://{super user}:{password}@localhost/{database name}'

if any error using `psycopg2-binary`
> 'postgresql+psycopg2://{super user}:{password}@localhost/{database name}'


if no error using `"psycopg[binary]"`
> 'postgresql://{super user}:{password}@localhost/{database name}'

if any error using `"psycopg[binary]"`
> 'postgresql+psycopg://{super user}:{password}@localhost/{database name}'

In case of passwords having special characters, need to encode the special character or use alternate way

For encoded, admin@12345 --> admin%4012345
```
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin%4012345@localhost/TodoApplicationDatabase'
```

Safer way
```
SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql",
    username="postgres",
    password="admin@12345",  # Use your actual password
    host="localhost",
    database="TodoApplicationDatabase",
)
```

* Also, update the below in the same file as `connect_args` is only for `SQLite`
> engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

to 

> engine = create_engine(SQLALCHEMY_DATABASE_URL)

* Now, we can run the appliation and test it.