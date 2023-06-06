from sqlalchemy import create_engine
from sqlalchemy import ForeignKey,Table,Column, Integer, String,CHAR
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

create_engine('sqlite:///Sports.db')

Base = declarative_base()


# wrestlers' table
class Wrestler(Base):
    __tablename__ = 'wrestlers'
    
    id = Column(Integer(), primary_key=True)
    firstName = Column(String())
    lastName = Column(Integer())
    age = Column(Integer())
    gender = Column(CHAR(1))


    def __repr__(self):
        return f'Wretler(id={self.id}, ' + \
            f'firstName={self.firstName}, ' +\
            f'lastName={self.lastName}, ' +\
            f'age={self.age}, ' +\
            f'gender={self}'

# championship table
class Stadium(Base):
    __tablename__ = 'stadiums'
    
    id = Column(Integer(), primary_key=True)
    Title = Column(String())
    country = Column(String())

    def __repr__(self):
        return f'Stadium(id={self.id}, ' + \
            f'Name={self.Name}, ' + \
            f'country={self.country}'

# stadium table
class Championship(Base):
    __tablename__ = 'championships'
    
    id = Column(Integer(), primary_key=True)
    Title = Column(String())
    # make = Column(String())

    def __repr__(self):
        return f'Championship(id={self.id}, ' + \
            f'Name={self.Title}, ' 
            # f'country={self.make}'

# match table
class  Match(Base):
    __tablename__ = 'matches'
    
    id = Column(Integer(), primary_key=True)
    category = Column(String())
    duration = Column(Integer())

    def __repr__(self):
        return f'Stadium(id={self.id}, ' + \
            f'category={self.Title}, ' + \
            f'duration={self.make}'

# review table
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    
    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'rating={self.rating},' + \
            f'restaurant_id={self.restaurant_id})'


if __name__ == '__main__':
    engine = create_engine('sqlite:///Sports.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    wrestler1 = Wrestler(firstName = "Dominik", lastName= " Mysterio", age= 23, gender= "M")
    wrestler2 = Wrestler(firstName = "Humberto", lastName= " Carrillo", age= 24, gender = "M")
    wrestler3 = Wrestler(firstName = "Liv", lastName= "Morgan", age= 26, gender= "F")
    wrestler4 = Wrestler(firstName = "Sonya", lastName= "Deville", age = 26, gender = "F")
    wrestler5 = Wrestler(firstName = "Angel", lastName= "Garza", age= 27, gender= "M")
    wrestler6 = Wrestler(firstName = "Alex", lastName= "Bliss", age = 29, gender = "F")
    wrestler7 = Wrestler(firstName = "Samy", lastName= "Zyne", age= 36, gender = "M")
    wrestler8 = Wrestler(firstName = "Kevin", lastName = "Owen", age= 36, gender = "M")
    wrestler9 = Wrestler(firstName = "Romain", lastName = "Reigns", age = 37, gender = "M")
    wrestler10 = Wrestler(firstName = "Seth", lastName = "Rollins", age = 34, gender = "M")

    stadium1 = Stadium(Title = "Bell_Centre", country = "Canada")
    stadium2 = Stadium(Title = "AT&T", country = "USA")
    stadium3 = Stadium(Title = "Alamodome", country = "USA")
    stadium4 = Stadium(Title = "Altice_Arena", country = "Portugal")
    stadium5 = Stadium(Title = "Ahoy_Rotterdam", country = "Netherlands")
    stadium6 = Stadium(Title = "Barclays_Center", country = "USA")

    match1 = Match(category = "ladder_match", duration = 45)
    match2 = Match(category = "Tag_team_match", duration = 20)
    match3 = Match(category = "Royal_Rumble", duration = 60)
    match4 = Match(category = "Elimination_match", duration = 50)
    match5 = Match(category = "Hell_in_cell", duration = 60)
    match6 = Match(category = "Money_in_the_Bank", duration = 30)

    championship1 = Championship(Title = "Heavyweight")
    championship2 = Championship(Title = "Intercontinental")
    championship3 = Championship(Title = "Universal")
    championship4 = Championship(Title = "United States")
    championship5 = Championship(Title = "Tag_team")


    session.add_all([wrestler1, wrestler2, wrestler3,wrestler4,wrestler5,wrestler6,wrestler7,wrestler8,wrestler9,wrestler10])
    session.add_all([stadium1,stadium1,stadium2,stadium3,stadium4,stadium5,stadium6])
    session.add_all([championship1,championship2,championship3,championship4,championship5])
    session.add_all([match1, match2, match3, match4, match5,match6])
    session.commit()

