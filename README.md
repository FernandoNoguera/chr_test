# chr test


### Create and activate your virtual enviroment

```
$ virtualenv .venv
$ source .venv/bin/activate
```

### Install all packages

```
$ pip install -r requirements.txt
```

### Create postgres user and database
`$ sudo -u posgres psql`

```sql
CREATE DATABASE db;
CREATE USER root WITH PASSWORD '1234';
ALTER ROLE root SET client_encoding TO 'utf8';
ALTER ROLE root SET default_transaction_isolation TO 'read committed';
ALTER ROLE root SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE api_db TO root;
```

### configure your .env file

```
$ cp core/.env.sample core/.env
```

### Run migrations on database

```
$ python manage.py migrate
```


### Run server

```
$ python manage.py runserver
```

### ROUTES URLS

Tarea 1:
http://localhost:8000/

Tarea 2:
http://localhost:8000/