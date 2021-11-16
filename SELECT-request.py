

import psycopg2

import sqlalchemy

# создаем engine
engine = sqlalchemy.create_engine('postgresql://romanp:__@localhost:5432/lesson3')
engine

# установим соединение
connection = engine.connect()



sel9 = connection.execute(""" SELECT album_name, year FROM albums
WHERE year=2018;""").fetchmany(10)
print(sel9)

sel10 = connection.execute(""" SELECT collection_name, year FROM collection
WHERE year BETWEEN 2018 AND 2020;""").fetchmany(10)
print(sel10)

sel11 = connection.execute(""" SELECT title, time FROM track
WHERE time >= 3.5 ;""").fetchmany(10)
print(sel11)

sel12 = connection.execute(""" SELECT title FROM track
WHERE title LIKE '%%My%%' ;""").fetchmany(10)
print(sel12)

sel13 = connection.execute(""" SELECT name FROM artist
WHERE name NOT LIKE '%% %%' ;""").fetchmany(10)
print(sel13)

sel14 = connection.execute(""" SELECT title, time FROM track
ORDER BY time DESC ;""").fetchmany(1)
print(sel14)