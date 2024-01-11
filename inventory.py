# importing necessary libraries/modules
import sqlite3
from sqlalchemy.sql import func
from sqlalchemy import create_engine, select
from sqlalchemy import ForeignKey,Table,Column, Integer, String,CHAR
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# CREATE A NEW ENGINE INSTANCE
create_engine('sqlite:///Inventory.db')
# create class contains a MetaData object where newly defined Table objects are collected.
Base = declarative_base()


# product's table
class Product(Base):
    # table name, columns
    __tablename__ = 'products'
    
    id = Column(Integer(), primary_key=True)
    productName = Column(String())
    description = Column(String())
    QuantityInStock = Column(Integer())

    manufacturer_id = Column(Integer(), ForeignKey('manufacturers.id'))
    category_id = Column(Integer(), ForeignKey('categories.id'))

    transactions = relationship('Transaction', backref=backref('product'))

   
    # __repr__. represent a class's objects as a string. 
    def __repr__(self):
        return f'Product(id={self.id}, ' + \
            f'productName={self.productName}, ' 
            

# manufacturer's table
class Manufacturer(Base):
    # table name, columns
    __tablename__ = 'manufacturers'
    
    id = Column(Integer(), primary_key=True)
    Title = Column(String())
    contactPerson = Column(String())
    
    products = relationship('Product', backref=backref('manufacturer'))
    # championships = relationship('Championship', backref=backref('stadium'))

#  represent a class's objects as a string.
    def __repr__(self):
        return f'Manufacter(id={self.id}, ' + \
            f'Title={self.Title}, '
         

# Category's table
class Category(Base):
    # table name, columns
    __tablename__ = 'categories'
    
    id = Column(Integer(), primary_key=True)
    categoryName = Column(String())
    description = Column(String())

    products = relationship('Product', backref=backref('category'))

    #  represent a class's objects as a string.
    def __repr__(self):
        return f'Category(id={self.id}, ' + \
            f'categoryName={self.categoryName}, ' 

# Transaction table
class  Transaction(Base):
    # table name, columns
    __tablename__ = 'transactions'
    
    id = Column(Integer(), primary_key=True)
    transactionType = Column(String(255))

    product_id = Column(Integer(), ForeignKey('products.id'))
#  represent a class's objects as a string.
    def __repr__(self):
        return f'Stadium(id={self.id}, ' 
            

# user table
class User(Base):
    # table name, columns
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    userName = Column(Integer())
    firstName = Column(String())
    lastName = Column(String())
    pnoneNo = Column(String())
    #  represent a class's objects as a string.
    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'userName={self.userName},' 
       
        


if __name__ == '__main__':
    engine = create_engine('sqlite:///Inventory.db')
    Base.metadata.create_all(engine)
    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()

# CREATING products
#     wrestler1 = Wrestler(firstName = "Dominik", lastName= " Mysterio", age= 23, gender= "M")
#     wrestler2 = Wrestler(firstName = "Humberto", lastName= " Carrillo", age= 24, gender = "M")
#     wrestler3 = Wrestler(firstName = "Liv", lastName= "Morgan", age= 26, gender= "F")
#     wrestler4 = Wrestler(firstName = "Sonya", lastName= "Deville", age = 26, gender = "F")
#     wrestler5 = Wrestler(firstName = "Angel", lastName= "Garza", age= 27, gender= "M")
#     wrestler6 = Wrestler(firstName = "Alex", lastName= "Bliss", age = 29, gender = "F")
#     wrestler7 = Wrestler(firstName = "Samy", lastName= "Zyne", age= 36, gender = "M")
#     wrestler8 = Wrestler(firstName = "Kevin", lastName = "Owen", age= 36, gender = "M")
#     wrestler9 = Wrestler(firstName = "Romain", lastName = "Reigns", age = 37, gender = "M")
#     wrestler10 = Wrestler(firstName = "Seth", lastName = "Rollins", age = 34, gender = "M")
#     wrestler11 = Wrestler(firstName = "Rey", lastName = " Mysterio", age = 48, gender = "M")
# # CREATING manufacturers
#     stadium1 = Stadium(Title = "Bell_Centre", country = "Canada")
#     stadium2 = Stadium(Title = "AT&T", country = "USA")
#     stadium3 = Stadium(Title = "Alamodome", country = "USA")
#     stadium4 = Stadium(Title = "Altice_Arena", country = "Portugal")
#     stadium5 = Stadium(Title = "Ahoy_Rotterdam", country = "Netherlands")
#     stadium6 = Stadium(Title = "Barclays_Center", country = "USA")
# # CREATING categories
#     match1 = Match(category = "ladder_match", duration = 45, championship_id = 3)
#     match2 = Match(category = "Tag_team_match", duration = 20, championship_id = 2)
#     match3 = Match(category = "Royal_Rumble", duration = 60, championship_id = 3)
#     match4 = Match(category = "Elimination_match", duration = 50, championship_id = 4)
#     match5 = Match(category = "Hell_in_cell", duration = 60, championship_id = 2)
#     match6 = Match(category = "Money_in_the_Bank", duration = 30, championship_id = 1)
# # CREATING Transactions
#     championship1 = Championship(Title = "Heavyweight", stadium_id = 1)
#     championship2 = Championship(Title = "Intercontinental", stadium_id = 4)
#     championship3 = Championship(Title = "Universal", stadium_id = 3)
#     championship4 = Championship(Title = "United States", stadium_id = 4)
#     championship5 = Championship(Title = "Tag_team", stadium_id = 5)
# # USERS
#     review1 =  Review(rating = 5,match_id =4, wrestler_id = 4)
#     review2 =  Review(rating = 4,match_id =1, wrestler_id = 3 )
#     review3 =  Review(rating = 4,match_id =2, wrestler_id = 6)
#     review4 =  Review(rating = 3,match_id =4, wrestler_id = 4)
#     review5 =  Review(rating = 5,match_id =3, wrestler_id = 10)

# # ADDING THE SESSION TO DATABASE AND COMMMITTING CHANGES
#     session.add_all([wrestler1, wrestler2, wrestler3,wrestler4,wrestler5,wrestler6,wrestler7,wrestler8,wrestler9,wrestler10,wrestler11])
#     session.add_all([stadium1,stadium1,stadium2,stadium3,stadium4,stadium5,stadium6])
#     session.add_all([championship1,championship2,championship3,championship4,championship5])
#     session.add_all([match1, match2, match3, match4, match5,match6])
#     session.add_all([review1,review2,review3,review4,review5])
#     session.commit()

# CREATING USER MENU 
def main():
# choices starts from 0
# use a while_loop to loop through
    choice = 0
    while choice !=10:
        print("Welcome to the SITE!")
        print("1) All the wrestlers")
        print("2) Wrestler 27 years old and above ")
        print("3) Wrestler below 27 years old ")
        print("4) average of the rating")
        print("5) all Stadium")
        # print("6) order in ascending order")
        print("7) search a wrestler")
        print("8) search rating of certain wrestler")
        print("9) search by id")
        print("10) Quit ")
        # print("11) add into")
# prompt the user to type an input.
        choice = int(input())
        # choice += 1 

# returns a LIST
        if choice == 1:
            print("***All wrestlers***")
            wrestlers = session.query(Wrestler).all()
            for wrestler in wrestlers:
                print([wrestler.firstName + ' '+ wrestler.lastName])

#  returns a list of filtered data
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
       
# calculates the average reviews
        elif choice == 4:
            print("****Printing Average Rating****")
            hello = average_rating = session.query(func.avg(Review.rating)).scalar()
            print(" AVERAGE RATE IS" + " " +  str(hello))    

        # Edited
        elif choice == 5:
            print("****All the stadium and the countries ****")
            stadiums = session.query(Stadium).all()
            for stadium in stadiums:
                print("Title:",  stadium.Title, "Country:", stadium.country)

        # elif choice == 6:
        #     list1 = session.query(Review).order(Review.rating)
        #     for review in list1:
        #         print(list1)

# returns a tuple
        elif choice == 7:
            print ("****Select wresler of choice****")
            user_input = input("Enter the wrestler.lastName:")
            wrestlers = session.query(Wrestler).filter(Wrestler.lastName == user_input)
           
            for wrestler in wrestlers:
              print (("id:", wrestler.id, "Name:", wrestler.firstName, wrestler.lastName, "Age:", wrestler.age, "Gender:", wrestler.gender))
        
        elif choice == 8:
            print ("****Select rating of a wrestler****")
            user_input = input("Enter the wrestles id:")
            wrestlers = session.query(Review).filter(Review.wrestler_id == user_input)
            for review in wrestlers:
              print("id:", review.id, "rating:", review.rating)  

        elif choice == 9:
            print("*****select by id****")
            my_user = session.get(Match,6)
            print(my_user.category)
#  quit
        elif choice == 10:
            print("You have left the main Menu")
            print("to get back to the main Menu type: python3 main.py")

        # elif choice == 11:
        #     print("***Add into***")
        #     sinput = input("Enter the stadium, country:")
        #     # stadiums = session.query(Stadium).
        #     stadiums = Stadium(Stadium.Title==sinput, Stadium.country==sinput)
            
        #     session.add_all(stadiums)
        #     # session.add_all( Stadium.Title,Stadium.country)
        #     session.commit()



# calling the function
if __name__ == "__main__":
    main()

