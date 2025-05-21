# SQL

- Structured English Query Language

## PostgreSQL

- PostgreSQL (family of related  RDBMS tools & a dialect of SQL)
- RDBMS : relational database management systems
- `postgres` : a program that runs the postgres server
- `psql` : a CLI tool for communicating with a postgres server
- `database` : a structured storage of data
  - relational database: a set of inter-linked tables storing data
- `postgres (database)` : the default postgres database 
- `table` stores information about 1 thing
- `schema` : a division of a database that tables can be inside
  - `public` : default schema

## `psql` commands

- `\q` to quit
- `\l` to view databases
- `\dt` to view tables in the current database
- `\c` to connect to another database

## SQL keywords

- `SELECT` : give me data (these columns)
  - `AS` : rename something temporarily
- `FROM` : from where should the data be got
  - `JOIN` : add this table on
- `WHERE` : filter the rows based on this condition
  - `LIKE`
  - `ILIKE`
  - `OR`, `AND`, `NOT`
  - `IN`
  - `BETWEEN`
- `GROUP BY` : bundle up the rows based on this shared characteristic
- `ORDER BY` : Sort the data by a column
  - `ASC`
  - `DESC`
- `LIMIT` : only this many rows

```sql
select movie_id, character_name
from movie_cast
JOIN movie
    ON (movie_cast.movie_id = movie.movie_id)
LIMIT 5
OFFSET 1035
```

```sql
SELECT
    EXTRACT(year FROM release_date) AS release_year, -- Get the year from the date and rename it
    AVG(budget) -- average up all the values in the bucket
FROM movie
GROUP BY EXTRACT(year FROM release_date) -- put all rows with the same characterstic into a bucket
;
```