from sqlalchemy.orm import relationship

from database import Base

from sqlalchemy import Column, Integer, String, Time, ForeignKey, Table, LargeBinary

user_anime_table = Table("user_anime",Base.metadata,Column('user_id', Integer, ForeignKey('users.id')),
                         Column('anime_id', Integer, ForeignKey('anime.id')))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    avatar = Column(String)
    password = Column(String(255), nullable=False)

    anime_list = relationship("Anime", secondary=user_anime_table, back_populates="users")


class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    time_stop = Column(Integer)
    number_episode = Column(Integer)

    users = relationship("User", secondary=user_anime_table, back_populates="anime_list")

    