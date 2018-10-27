from sqlalchemy import create_engine, Column, String, Integer, BLOB, ForeignKey, Binary
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy_imageattach.entity import image_attachment, Image
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///tut.db', echo=False)
Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    std_id = Column('index_no', String(20))
    hall = Column('hall_of_residence', String)
    wing = Column('wing', String)

    def __init__(self, name, std_id, hall, wing):
        self.name = name
        self.std_id = std_id
        self.hall = hall
        self.wing = wing



''' class Polls(Base):
    __tablename__ = 'polls'

    polls_id = Column('polls_id', Integer, primary_key=True)
    name = Column('name', String)
    position = Column('position', String)
    # votes = Column('votes', Integer)
    # img = Column('image', BLOB) #check up on this one

    def __init__(self, name, position, votes):
        self.name = name
        self.position = position
        self.votes = votes
 '''

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column('name',String)
    pic = Column('pic', Binary)

    def __init__(self, name, pic):
        self.name = name
        self.pic = pic
    

Base.metadata.create_all(engine)