## Introduction

![alt text](./productoin-DBMS-images/mysql-intro.png)

* [_setup MySQL_](#setup-and-installation)
* [_create a table_](#create-a-database-table)
* [_connect to FastAPI_](#connect-to-fastapi)


### Setup and Installation

* Go to &rarr; https://www.mysql.com/ &rarr; click on `Downloads` &rarr; under `MySQL Community Edition` select `MySQL Community (GPL) Downloads »` &rarr; select `MySQL Community Server` &rarr; select the older version `8.0.x` from drop down and click on `Go to download page` &rarr; click on download for `Windows (x86, 32-bit), MSI Installer` (This is for testing, lighter version) &rarr; click on `No thanks, just start my download`.

* Open the installer, select the `Developer Default` (this might be deprecated)

![alt text](./productoin-DBMS-images/mysql-1.png)

Follow the instructions to complete the installation (can watch the lecture)

* Launch the workbench

### Create a database table

watch the lecture

### Connect to FastAPI

watch the lecture

* Install python library `pymysql`

```
pip install pymysql
```

* Now update the database URL `SQLALCHEMY_DATABASE_URL` that was used for SQLite DB for earlier exercise in `database.py`. Can comment it and add another one for `MySQL`
> 'mysql+pymysql://root:{password}@127.0.0.1:3306/{database name}'

>root -- root user of MySQL

>127.0.0.1 -- means the local host