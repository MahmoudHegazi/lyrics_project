#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

"""File name: database_setup.py

That's Database Setup file:
    1. run this file to setup your database
    2. run after this lotsofcar.py    

More details can be found in the README.md file,
which is included with this project.
"""


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(400))


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)    
   


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,            
        }


class Song(Base):
    __tablename__ = 'song'
    
    name = Column(String(300), nullable=False)
    id = Column(Integer, primary_key=True)
    lyrics = Column(String(5000), nullable=False)
    pic = Column(String(500), nullable=False)
    actor = Column(String(300), nullable=False)
    year = Column(String(4))
    song_link = Column(String(600))
    views = Column(Integer)    
    menu_id = Column(Integer, ForeignKey('menu.id'))
    menu = relationship(Menu)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'lyrics': self.lyrics,
            'id': self.id,
            'pic': self.pic,
            'actor': self.actor,
            'views': self.views,
            'year': self.year,
        }
    

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    content = Column(String(1000))
    creator_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    song_id = Column(Integer, ForeignKey('song.id'))
    song = relationship(Song)



engine = create_engine('sqlite:///lyrics.db')
Base.metadata.create_all(engine)
