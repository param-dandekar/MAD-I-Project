from bin import DATABASE
from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(32), nullable=False)
    role_id = Column(Integer, ForeignKey('role.role_id'))
    password = Column(String(32), nullable=False, default='password')
    email = Column(String(32))
    profile_photo = Column(Text, default='default_pic.jpg')
    about_me = Column(Text)


class Role(Base):
    __tablename__ = 'role'
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(32), unique=True, nullable=False)

class Album(Base):
    __tablename__ = 'album'
    album_id = Column(Integer, primary_key=True, autoincrement=True)
    artist_id = Column(Integer, ForeignKey('user.user_id'))
    album_name = Column(String(32), nullable=False)
    genre = Column(String(32))

class Song(Base):
    __tablename__ = 'song'
    song_id = Column(Integer, primary_key=True, autoincrement=True)
    album_id = Column(Integer, ForeignKey('album.album_id'))
    song_name = Column(String(32), nullable=False)
    song_file = Column(Text)
    lyrics = Column(Text)
    duration = Column(Integer)
    release_date = Column(Date)

class Playlist(Base):
    __tablename__ = 'playlist'
    playlist_id = Column(Integer, primary_key=True, autoincrement=True)
    creator_id = Column(Integer, ForeignKey('user.user_id'))
    public = Column(Boolean, nullable=False)
    creation_date = Column(Date)

class PlaylistSong(Base):
    __tablename__ = 'playlist_song'
    __table_args__ = (
        PrimaryKeyConstraint('playlist_id', 'song_id'),
    )
    playlist_id = Column(Integer, ForeignKey('playlist.playlist_id'))
    song_id = Column(Integer, ForeignKey('song.song_id'))
    position = Column(Integer, nullable=False)
    
from sqlalchemy import create_engine

engine = create_engine(f'{DATABASE}')
