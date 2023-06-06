from main import session,Wrestler, Championship, Stadium, Match, Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


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


if __name__ == '__main__':
    engine = create_engine('sqlite:///Sports.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.add_all([wrestler1, wrestler2, wrestler3,wrestler4,wrestler5,wrestler6,wrestler7,wrestler8,wrestler9,wrestler10])
session.commit()


