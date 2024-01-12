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
    phoneNo = Column(String())
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
    product1 = Product(productName = "Laptop", description= " High-performance ", QuantityInStock= 50, manufacturer_id= 1, category_id= 1)
    product2 = Product(productName = "Smartphone", description= " 6-inch display ", QuantityInStock= 100, manufacturer_id= 2, category_id= 2)
    product3 = Product(productName = "Printer", description= " Wireless, color ", QuantityInStock= 20, manufacturer_id= 3, category_id= 3)
    product4 = Product(productName = "Headphones", description= " Noise-canceling ", QuantityInStock= 30, manufacturer_id= 1, category_id= 4)
    product5 = Product(productName = "Tablet", description= " 10-inch screen ", QuantityInStock= 25, manufacturer_id= 2, category_id= 2)

# # CREATING manufacturers
    man1 = Manufacturer(Title = "ABC Electronics", contactPerson = "John Doe")
    man2 = Manufacturer(Title = "XYZ Mobile", contactPerson = "Jane Smith")
    man3 = Manufacturer(Title = "PrintTech", contactPerson = "Mark Jackson")
    man4 = Manufacturer(Title = "Tech innovators", contactPerson = "Sarah Lee")
    man5 = Manufacturer(Title = "Mega Electronics", contactPerson = "James Wong")


# # CREATING categories
    category1 = Category(categoryName = "Electronics", description = " Electronic devices ")
    category2 = Category(categoryName = "Mobile", description = " Smartphones and tablets ")
    category3 = Category(categoryName = "Office", description = " Office equipment ")
    category4 = Category(categoryName = "Appliances", description = " Home appliances ")
    category5 = Category(categoryName = "Clothing", description = " Apparel and accessories ")
# # CREATING Transactions
    transaction1 = Transaction(transactionType = "Purchase", product_id = 1)
    transaction2 = Transaction(transactionType = "Sale", product_id = 2)
    transaction3 = Transaction(transactionType = "Return", product_id = 3)
    transaction4 = Transaction(transactionType = "Sale", product_id = 1)
    transaction5 = Transaction(transactionType = "Purchase", product_id = 2)
# # USERS
    user1 =  User(userName = "admin",  firstName="Admin", lastName = "User", phoneNo="+323456788")
    user2 =  User(userName = "staff1",  firstName="Joan", lastName = "Dough", phoneNo="+25498909093")
    user3 =  User(userName = "staff2",  firstName="Jane", lastName = "Jones", phoneNo="+8784798357")
    user4 =  User(userName = "user3",  firstName="Emma", lastName = "White", phoneNo="+09045874382")
    user5 =  User(userName = "manager",  firstName="Wong", lastName = "Lee", phoneNo="+36767980")



# # ADDING THE SESSION TO DATABASE AND COMMMITTING CHANGES
    session.add_all([product1, product2, product3, product4, product5])
    session.add_all([category1, category2, category3, category4, category5])
    session.add_all([man1, man2, man3, man4, man5])
    session.add_all([transaction1, transaction2, transaction3, transaction4, transaction5])
    session.add_all([user1, user2,user3, user4,user5])
    session.commit()

# CREATING USER MENU 
def main():
# choices starts from 0
# use a while_loop to loop through
    choice = 0
    while choice !=10:
        print("Welcome to our Inventory!")
        print("1) All the products")
        print("2) Products whose quantity in Stocks are below 50 ")
        print("3) average of Quantity in Stock")
        print("4) search a transaction type")
        print("5) Quit ")
        # print("11) add into")
# prompt the user to type an input.
        choice = int(input())
        # choice += 1 

# returns a LIST
        if choice == 1:
            print("***All Products***")
            products = session.query(Product).all()
            for product in products:
                print([product.productName + ' '+ product.description ])

#  returns a list of filtered data
        elif choice == 2:
            print("****Products whose Quantity in stocks are below 50*****")
            products = session.query(Product).filter( Product.QuantityInStock < 50)
            for product in products:
                print(product.productName, product.QuantityInStock )
                
        
# calculates the average quantity
        elif choice == 3:
            print("****Printing Average quantity in stock****")
            hello = average_stock = session.query(func.avg(Product.QuantityInStock)).scalar()
            print(" AVERAGE QUANTITY IN STOCK IS" + " " +  str(hello))    


# returns a tuple
        elif choice == 4:
            print ("****Searching for transaction type****")
            user_input = input("Enter the transaction type:")
            transactions = session.query(Transaction).filter(Transaction.transactionType == user_input)
           
            for transaction in transactions:
              print (("id:", transaction.id, "Name:", transaction.transactionType ))

        
        
#  quit
        elif choice == 5:
            print("You have left the main Menu")
            print("to get back to the main Menu type: python3 main.py")

        else:
            print("Incorrect input")

      

# calling the function
if __name__ == "__main__":
    main()

