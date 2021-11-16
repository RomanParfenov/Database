
import psycopg2

import sqlalchemy

# создаем engine
engine = sqlalchemy.create_engine('postgresql://romanp:__@localhost:5432/lesson3')
engine

# Соединение
connection = engine.connect()

sel1 = connection.execute("""INSERT INTO genre (genreid, genre_name) VALUES ('1','electronic music'), ('2','rock'),
('3','chanson'), ('4','country pop'), ('5','rap');""")

sel2 = connection.execute("""INSERT INTO artist (artistid, name) VALUES ('1','DJ Tiesto'), ('2','Armin Van Buuren'),
('3','Scorpions'), ('4','Metallica'), ('5','Pink Floyd'), ('6','Shufutinsky Mikhail'),
('7','Kelly Clarkson'), ('8','Eminem');""")

sel3 = connection.execute("""INSERT INTO artistgenre (genreid, artistid) VALUES ('1','1'), ('1','2'), ('1','3'),
('2','3'), ('2','4'), ('2','5'), ('3','6'), ('3','7'), ('4','7'), ('5','8');""")

sel4 = connection.execute("""INSERT INTO albums (albumid, album_name, year)
VALUES ('1', 'In My Memory', '2001'), ('2', 'Mirage', '2010'), ('3', 'Embrace', '2018'),
('4', 'Euthymia', '2020'), ('5', 'Live Bites', '1995'), ('6', 'Return to Forever', '2012'),
('7', 'Metallica', '1993'), ('8', 'The Division Bell', '1994'), ('9', 'The Best', '2020'),
('10', 'Breakaway', '2006'), ('11', 'Encore', '2007');""")

sel5 = connection.execute("""INSERT INTO albumsartist (artistid, albumid) VALUES ('1','1'), ('2','2'), ('2','3'),
('2','4'), ('3','5'), ('3','6'), ('4','7'), ('5','8'), ('6','9'), ('7','10'), ('8','11');""")

sel6 = connection.execute("""INSERT INTO track (trackid, albumid, title, time)
VALUES ('1','1', 'Magik Journey', '9.19'), ('2','1', 'Close to You', '5.03'), ('3','1', 'In My Memory', '6.05'),
('4','1', 'Suburban Train', '9.23'), ('5','2', 'Mirage', '2.08'), ('6','2', 'This Light Between Us', '5.09'),
('7','2', 'Orbion', '5.17'), ('8','3', 'Face 0f Summer', '6.38'), ('9','3', 'Make it Right', '5.41'),
('10','4', 'Euthymia', '3.21'), ('11','5', 'Rhythm of Love', '3.45'), ('12','5', 'Wind of Change', '5.47'),
('13','5', 'Living for Tomorrow', '6.55'), ('14','6', 'All for One', '2.58'), ('15','6', 'Eye of the Storm', '4.27'),
('16','7', 'Nothing Else Matters', '6.28'), ('17','7', 'Unforgiven', '6.23'), ('18','8', 'High Hopes', '8.32'),
('19','9', 'Marjanja', '3.20'), ('20','10', 'Breakaway', '3.58'), ('21','11', 'Mockingbird', '4.11');""")

sel7 = connection.execute("""INSERT INTO collection (collectionid, collection_name, year)
VALUES ('1', 'Freedom', '2018'), ('2', 'Electro', '2015'), ('3', 'New era', '2020'),
('4', 'Collection', '2019'), ('5', 'Forward', '2005'), ('6', 'Rock exchange', '2011'),
('7', 'Sunrise', '2003'), ('8', 'Other', '2011');""")

sel8 = connection.execute("""INSERT INTO trackcollection (trackid, collectionid) VALUES ('18','1'), ('12','1'), 
('7','1'), ('2','2'), ('4','2'), ('13','2'), ('6','3'), ('18','3'), ('11','3'), ('21','4'), ('19','4'),
('3','4'), ('12','5'), ('16','5'), ('6','5'), ('13','6'), ('15','6'), ('17','6'), ('18','6'), ('6','7'), 
('15','7'), ('19','7'), ('5','8'), ('21','8'), ('20','8'), ('19','8');""")

