CREATE TABLE artists (
    id INTEGER PRIMARY KEY ASC,
    artist_name TEXT
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY ASC,
    album_title TEXT,
    artist_name TEXT
);

CREATE TABLE songs(
    id INTEGER PRIMARY KEY ASC,
    song_title TEXT,
    album_title TEXT,
    track_no INTEGER,
    track_length INTEGER
);

