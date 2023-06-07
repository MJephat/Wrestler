import sqlite3
from sqlalchemy.sql import func
from sqlalchemy import create_engine, select
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

    reviews = relationship('Review', backref=backref('wrestler'))

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
    championships = relationship('Championship', backref=backref('stadium'))


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
    matches = relationship('Match', backref=backref('championship'))
    stadium_id = Column(Integer(), ForeignKey('stadiums.id'))
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
    championship_id = Column(Integer(), ForeignKey('championships.id'))
    reviews = relationship('Review', backref=backref('match'))

    def __repr__(self):
        return f'Stadium(id={self.id}, ' + \
            f'category={self.Title}, ' + \
            f'duration={self.make}'

# review table
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    match_id = Column(Integer(), ForeignKey('matches.id'))
    wrestler_id = Column(Integer(), ForeignKey('wrestlers.id'))
    
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

    match1 = Match(category = "ladder_match", duration = 45, championship_id = 3)
    match2 = Match(category = "Tag_team_match", duration = 20, championship_id = 2)
    match3 = Match(category = "Royal_Rumble", duration = 60, championship_id = 3)
    match4 = Match(category = "Elimination_match", duration = 50, championship_id = 4)
    match5 = Match(category = "Hell_in_cell", duration = 60, championship_id = 2)
    match6 = Match(category = "Money_in_the_Bank", duration = 30, championship_id = 1)

    championship1 = Championship(Title = "Heavyweight", stadium_id = 1)
    championship2 = Championship(Title = "Intercontinental", stadium_id = 4)
    championship3 = Championship(Title = "Universal", stadium_id = 3)
    championship4 = Championship(Title = "United States", stadium_id = 4)
    championship5 = Championship(Title = "Tag_team", stadium_id = 5)

    review1 =  Review(rating = 5,match_id =4, wrestler_id = 4)
    review2 =  Review(rating = 4,match_id =1, wrestler_id = 3 )
    review3 =  Review(rating = 4,match_id =2, wrestler_id = 6)
    review4 =  Review(rating = 3,match_id =4, wrestler_id = 4)
    review5 =  Review(rating = 5,match_id =3, wrestler_id = 10)


    session.add_all([wrestler1, wrestler2, wrestler3,wrestler4,wrestler5,wrestler6,wrestler7,wrestler8,wrestler9,wrestler10])
    session.add_all([stadium1,stadium1,stadium2,stadium3,stadium4,stadium5,stadium6])
    session.add_all([championship1,championship2,championship3,championship4,championship5])
    session.add_all([match1, match2, match3, match4, match5,match6])
    session.add_all([review1,review2,review3,review4,review5])
    session.commit()

def main():

    choice = 0
    while choice !=10:
        print("Welcome to the SITE!")
        print("1) All the wrestlers")
        print("2) Wrestler 27 years old and above ")
        print("3) Wrestler below 27 years old ")
        print("4) average of the rating")
        print("5) all Stadium")
        print("6) order in ascending order")
        print("7) search a wrestler")
        print("8) search rating of certain wrestler")
        print("10) Quit ")
        choice = int(input())
        # choice += 1 

        if choice == 1:
            print("***All wrestlers***")
            wrestlers = session.query(Wrestler).all()
            for wrestler in wrestlers:
                print(wrestler.firstName + ' '+ wrestler.lastName)

        elif choice == 2:
            print("****wrestler above 27 years old*****")
            wrestlers = session.query(Wrestler).filter( Wrestler.age >= 27)
            for wrestler in wrestlers:
                print(wrestler.firstName + ' '+ wrestler.lastName)
                
        elif choice == 3:
            print("****Wrestler below 27 years old****")
            wrestlers = session.query(Wrestler).filter( Wrestler.age < 27)
            for wrestler in wrestlers:
                print(wrestler.firstName + ' '+ wrestler.lastName)
       
        # Edited
        elif choice == 4:
            print("****Printing Average Rating****")
            hello = average_rating = session.query(func.avg(Review.rating)).scalar()
            print(" AVERAGE RATE IS" + " " +  str(hello))    

        # Edited
        elif choice == 5:
            print("****All the stadium and the countries ****")
            stadiums = session.query(Stadium).all()
            for stadium in stadiums:
                print(stadium.Title, stadium.country)

        elif choice == 6:
            list1 = session.query(Review).select(Review.rating)
            for review in list1:
                print(list1)
                
        elif choice == 7:
            print ("****Select wresler of choice****")
            user_input = input("Enter the wrestles wrestler.firstName:")
            wrestlers = session.query(Wrestler).filter(Wrestler.firstName == user_input)
            for wrestler in wrestlers:
              print ("id:", wrestler.id, "Name:", wrestler.firstName, wrestler.lastName, "Age:", wrestler.age, "Gender:", wrestler.gender)
        
        elif choice == 8:
            print ("****Select rating of a wrestler****")
            user_input = input("Enter the wrestles name:")
            wrestlers = session.query(Review).filter(Review.wrestler_id == user_input)
            for review in wrestlers:
              print("id:", review.id, "rating:", review.rating)  





if __name__ == "__main__":
    main()

