-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION postgres;

-- DROP SEQUENCE public.albums_albumid_seq;

CREATE SEQUENCE public.albums_albumid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.artist_artistid_seq;

CREATE SEQUENCE public.artist_artistid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.collection_collectionid_seq;

CREATE SEQUENCE public.collection_collectionid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.genre_genreid_seq;

CREATE SEQUENCE public.genre_genreid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.track_trackid_seq;

CREATE SEQUENCE public.track_trackid_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- public.albums definition

-- Drop table

-- DROP TABLE public.albums;

CREATE TABLE public.albums (
	albumid serial4 NOT NULL,
	album_name varchar(60) NOT NULL,
	"year" int4 NULL,
	CONSTRAINT albums_pkey PRIMARY KEY (albumid)
);


-- public.artist definition

-- Drop table

-- DROP TABLE public.artist;

CREATE TABLE public.artist (
	artistid serial4 NOT NULL,
	"name" varchar(60) NOT NULL,
	CONSTRAINT artist_pkey PRIMARY KEY (artistid)
);


-- public.collection definition

-- Drop table

-- DROP TABLE public.collection;

CREATE TABLE public.collection (
	collectionid serial4 NOT NULL,
	collection_name varchar(60) NOT NULL,
	"year" int4 NULL,
	CONSTRAINT collection_pkey PRIMARY KEY (collectionid)
);


-- public.genre definition

-- Drop table

-- DROP TABLE public.genre;

CREATE TABLE public.genre (
	genreid serial4 NOT NULL,
	genre_name varchar(60) NOT NULL,
	CONSTRAINT genre_pkey PRIMARY KEY (genreid)
);


-- public.albumsartist definition

-- Drop table

-- DROP TABLE public.albumsartist;

CREATE TABLE public.albumsartist (
	artistid int4 NOT NULL,
	albumid int4 NOT NULL,
	CONSTRAINT pkaa PRIMARY KEY (artistid, albumid),
	CONSTRAINT albumsartist_albumid_fkey FOREIGN KEY (albumid) REFERENCES public.albums(albumid),
	CONSTRAINT albumsartist_artistid_fkey FOREIGN KEY (artistid) REFERENCES public.artist(artistid)
);


-- public.artistgenre definition

-- Drop table

-- DROP TABLE public.artistgenre;

CREATE TABLE public.artistgenre (
	genreid int4 NOT NULL,
	artistid int4 NOT NULL,
	CONSTRAINT pkag PRIMARY KEY (genreid, artistid),
	CONSTRAINT artistgenre_artistid_fkey FOREIGN KEY (artistid) REFERENCES public.artist(artistid),
	CONSTRAINT artistgenre_genreid_fkey FOREIGN KEY (genreid) REFERENCES public.genre(genreid)
);


-- public.track definition

-- Drop table

-- DROP TABLE public.track;

CREATE TABLE public.track (
	trackid serial4 NOT NULL,
	albumid int4 NULL,
	title varchar(60) NOT NULL,
	"time" int4 NULL,
	CONSTRAINT track_pkey PRIMARY KEY (trackid),
	CONSTRAINT track_albumid_fkey FOREIGN KEY (albumid) REFERENCES public.albums(albumid)
);


-- public.trackcollection definition

-- Drop table

-- DROP TABLE public.trackcollection;

CREATE TABLE public.trackcollection (
	trackid int4 NOT NULL,
	collectionid int4 NOT NULL,
	CONSTRAINT pktc PRIMARY KEY (trackid, collectionid),
	CONSTRAINT trackcollection_collectionid_fkey FOREIGN KEY (collectionid) REFERENCES public.collection(collectionid),
	CONSTRAINT trackcollection_trackid_fkey FOREIGN KEY (trackid) REFERENCES public.track(trackid)
);


